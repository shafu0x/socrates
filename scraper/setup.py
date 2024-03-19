import os
from web3   import Web3
from dotenv import load_dotenv

load_dotenv("../.env")

CACHED        = True
RPC           = os.environ.get('RPC')
ETHERSCAN     = os.environ.get('ETHERSCAN_API_KEY')
ETHERSCAN_API = "https://api.etherscan.io/api"

w3 = Web3(Web3.HTTPProvider(RPC))
