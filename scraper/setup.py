import os
from web3   import Web3
from enum   import Enum
from dotenv import load_dotenv

load_dotenv("../.env")

CACHED        = True
DIR           = os.path.dirname(os.path.realpath(__file__))
CACHE         = DIR + "/.cache"
RPC           = os.environ.get('RPC')
ETHERSCAN     = os.environ.get('ETHERSCAN_API_KEY')
ETHERSCAN_API = "https://api.etherscan.io/api"

w3 = Web3(Web3.HTTPProvider(RPC))

if not os.path.exists(CACHE): os.makedirs(CACHE)

class Type(Enum):
    ETH_GLOBAL   = 0
    THE_BYTECODE = 1
