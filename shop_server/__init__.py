from flask import Flask
from data.transaction import Transaction, TransactionDto
import services.web3_service as sp
import services.monitoring as m
from db.database_mock import cart, products, transactions
import json
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)


@app.route('/product/<id>', methods=['POST'])
@cross_origin()
def add_product(id):
    casted_id = int(id)
    if products.keys().__contains__(casted_id):
        cart.products[casted_id] = products[casted_id]
        return cart.json(), 200
    else:
        return cart.json(), 404


@app.route('/product/<id>', methods=['DELETE'])
@cross_origin()
def remove_product(id):
    casted_id = int(id)
    if cart.products.keys().__contains__(casted_id):
        cart.products.pop(casted_id)
        return cart.json(), 200
    else:
        return cart.json(), 404


@app.route('/transaction', methods=['POST'])
@cross_origin()
def start_transaction():
    if len(cart.products) == 0:
        return "Cart is empty", 201
    public, private = sp.generate_account()
    transactions[public] = Transaction(public_key=public, private_key=private, cart=cart)
    with open('data.json', 'a', encoding='utf-8') as f:
        f.write(",")
        f.write(transactions[public].json())
    m.start_transaction_monitoring(transactions[public])
    return TransactionDto(public, transactions[public].get_price()).json(), 200


@app.route('/transaction/<p_key>', methods=['GET'])
@cross_origin()
def check_transaction(p_key):
    if transactions.keys().__contains__(p_key):
        return json.dumps(transactions[p_key].is_completed), 200
    else:
        return "No Transaction found", 404


if __name__ == '__main__':
    app.run(debug=True)


