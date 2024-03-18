from setup import env
from web3  import Web3

ADDRESS = '0xD152f549545093347A162Dce210e7293f1452150'
TX      = '0xdfe64868a256bfc7a2e4dc887983278b4801df9ffe0fc9989017ce1adb4521ba'

ABI = [
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

w3 = Web3(Web3.HTTPProvider(env('RPC')))

contract   = w3.eth.contract(address=ADDRESS, abi=ABI)
tx         = w3.eth.get_transaction(TX)
calldata   = tx['input']
decoded    = contract.decode_function_input(calldata)
recipients = decoded[1]['recipients']
print(recipients)
