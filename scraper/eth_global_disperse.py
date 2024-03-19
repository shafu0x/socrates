import requests
import pickle
from setup import *

CACHED_FILE = ".cache/eth_global_disperse.pkl"

ADDRESS  = '0xba17eeb3f0413b76184ba8ed73067063fba6e2eb'
DISPERSE = '0xD152f549545093347A162Dce210e7293f1452150'

params = {
    "module": "account",
    "action": "txlist",
    "address": ADDRESS,
    "apikey": ETHERSCAN
}

if not CACHED:
    response = requests.get(ETHERSCAN_API, params=params)
    with open(CACHED_FILE, "wb") as f:
        pickle.dump(response.json(), f)

if CACHED:
    with open(CACHED_FILE, "rb") as f:
        response = pickle.load(f)


txs = response["result"]
txs = [tx['hash'] for tx in txs if tx["to"].lower() == DISPERSE.lower()]

print(txs)
