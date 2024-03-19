from setup import *
from cache import *

CACHED_FILE = "eth_global.pkl"

ADDRESS = '0xD152f549545093347A162Dce210e7293f1452150'

ABI = [{"inputs": [{
            "name":"recipients",
            "type":"address[]"
         },
         {
            "name":"values",
            "type":"uint256[]"
         }
      ],
      "name":"disperseEther",
      "type":"function"
   }
]

def run(tx):
    if not CACHED:
        contract   = w3.eth.contract(address=ADDRESS, abi=ABI)
        tx         = w3.eth.get_transaction(tx)
        calldata   = tx['input']
        decoded    = contract.decode_function_input(calldata)
        recipients = decoded[1]['recipients']

        cache(CACHED_FILE, recipients)
        return recipients

    return load(CACHED_FILE)
