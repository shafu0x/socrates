from setup import *
from cache import *


ADDRESS = '0xD152f549545093347A162Dce210e7293f1452150'

ABI = [
   {
      "constant":False,
      "inputs":[
         {
            "name":"token",
            "type":"address"
         },
         {
            "name":"recipients",
            "type":"address[]"
         },
         {
            "name":"values",
            "type":"uint256[]"
         }
      ],
      "name":"disperseTokenSimple",
      "outputs":[
         
      ],
      "payable":False,
      "stateMutability":"nonpayable",
      "type":"function"
   },
   {
      "constant":False,
      "inputs":[
         {
            "name":"token",
            "type":"address"
         },
         {
            "name":"recipients",
            "type":"address[]"
         },
         {
            "name":"values",
            "type":"uint256[]"
         }
      ],
      "name":"disperseToken",
      "outputs":[
         
      ],
      "payable":False,
      "stateMutability":"nonpayable",
      "type":"function"
   },
   {
      "constant":False,
      "inputs":[
         {
            "name":"recipients",
            "type":"address[]"
         },
         {
            "name":"values",
            "type":"uint256[]"
         }
      ],
      "name":"disperseEther",
      "outputs":[
         
      ],
      "payable":True,
      "stateMutability":"payable",
      "type":"function"
   }
]

def run(tx):
    CACHED_FILE = f'eth_global_{tx}.pkl'

    if not CACHED:
        contract   = w3.eth.contract(address=ADDRESS, abi=ABI)
        tx         = w3.eth.get_transaction(tx)
        calldata   = tx['input']
        decoded    = contract.decode_function_input(calldata)
        recipients = decoded[1]['recipients']

        cache(CACHED_FILE, recipients)
        return recipients

    return load(CACHED_FILE)
