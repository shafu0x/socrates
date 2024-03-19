from setup import *
from cache import *
from abi.disperse import ABI

ADDRESS = '0xD152f549545093347A162Dce210e7293f1452150'

def run(tx, cached=CACHED):
    CACHED_FILE = f'eth_global_{tx}.pkl'

    if not cached:
        contract   = w3.eth.contract(address=ADDRESS, abi=ABI)
        tx         = w3.eth.get_transaction(tx)
        calldata   = tx['input']
        decoded    = contract.decode_function_input(calldata)
        recipients = decoded[1]['recipients']

        cache(CACHED_FILE, recipients)
        return recipients

    return load(CACHED_FILE)
