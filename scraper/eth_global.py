from setup import *
from cache import *

CACHED_FILE = "eth_global.pkl"

ADDRESS = '0xD152f549545093347A162Dce210e7293f1452150'
TX      = '0xdfe64868a256bfc7a2e4dc887983278b4801df9ffe0fc9989017ce1adb4521ba'

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

if not CACHED:
    contract   = w3.eth.contract(address=ADDRESS, abi=ABI)
    tx         = w3.eth.get_transaction(TX)
    calldata   = tx['input']
    decoded    = contract.decode_function_input(calldata)
    recipients = decoded[1]['recipients']

    cache(CACHED_FILE, recipients)

if CACHED: recipients = load(CACHED_FILE)

print(len(recipients))
