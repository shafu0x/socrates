import os
from web3   import Web3
from dotenv import load_dotenv

load_dotenv("../.env")

w3 = Web3(Web3.HTTPProvider(os.environ.get('RPC')))
