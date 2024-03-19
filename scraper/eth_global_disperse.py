import requests
from setup import *
from cache import *

CACHED_FILE = "eth_global_disperse.pkl"

ADDRESS  = '0xba17eeb3f0413b76184ba8ed73067063fba6e2eb'
DISPERSE = '0xD152f549545093347A162Dce210e7293f1452150'

params = {
    "module":  "account",
    "action":  "txlist",
    "address": ADDRESS,
    "apikey":  ETHERSCAN
}

def run():
    if not CACHED:
        response = requests.get(ETHERSCAN_API, params=params).json()
        txs = response["result"]
        txs = [tx['hash'] for tx in txs if tx["to"].lower() == DISPERSE.lower()]
        cache(CACHED_FILE, txs)
        return txs

    if CACHED: return load(CACHED_FILE)
