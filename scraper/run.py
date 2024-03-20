import pandas as pd
from setup               import Type
from eth_global          import run as get_recipients
from eth_global_disperse import run as get_txs

txs = get_txs()
recipients = []

for tx in txs: recipients.append(get_recipients(tx))

recipients = set([item for _ in recipients for item in _])

df = pd.DataFrame(recipients, columns=['address'])
df['type'] = Type.ETH_GLOBAL.value
df.to_csv('eth_global.csv', index=False)
