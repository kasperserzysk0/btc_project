from concurrent.futures import ThreadPoolExecutor
import shop_server.services.web3_service as bs
from data.transaction import Transaction

executor = ThreadPoolExecutor(max_workers=10)


def start_transaction_monitoring(transaction: Transaction):
    executor.submit(bs.monitor_transactions, transaction.public_key)

