import os
from web3   import Web3
from dotenv import load_dotenv

load_dotenv("../.env")

CACHED        = True
DIR           = os.path.dirname(os.path.realpath(__file__))
CACHED_DIR    = DIR + "/.cache"
RPC           = os.environ.get('RPC')
ETHERSCAN     = os.environ.get('ETHERSCAN_API_KEY')
ETHERSCAN_API = "https://api.etherscan.io/api"

w3 = Web3(Web3.HTTPProvider(RPC))

if not os.path.exists(CACHED_DIR): os.makedirs(CACHED_DIR)
