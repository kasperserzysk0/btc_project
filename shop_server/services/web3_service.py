from web3 import Web3
from eth_account import Account
from db.database_mock import transactions
import time

w3 = Web3(Web3.WebsocketProvider("ws://ws.cdf0jqpm17babkjy59e4xqgy8.blockchainnodeengine.com?key=AIzaSyDq41G8TRSPoy2C9UhqQwOkgOafY7WveEM"))

timeout = 600


def generate_account():
    Account.enable_unaudited_hdwallet_features()
    acct = Account.create()
    print(acct.key.hex())
    print(acct.address)
    return acct.address, acct.key.hex()


def monitor_transactions(public_key: str):
    trans = transactions[public_key]
    balance = 0
    hashes = set()
    timeout_at = time.time() + timeout

    while True:
        block = w3.eth.get_block('latest')
        for tx_hash in block.transactions:
            tx = w3.eth.get_transaction(tx_hash)
            if time.time() > timeout_at:
                trans.is_completed = "TIME_OUTED"
                print("TRANSACTION TIME OUT")
                return
            if tx['to'] == trans.public_key:
                if tx['blockHash'] not in hashes:
                    hashes.add(tx['blockHash'])
                    balance += tx['value']
                if balance >= w3.to_wei(trans.get_price(), 'ether'):
                    print("TRANSACTION SUCCEEDED")
                    trans.is_completed = "SUCCESS"
                    return
        if time.time() > timeout_at:
            trans.is_completed = "TIME_OUTED"
            print("TRANSACTION TIME OUT")
            return

