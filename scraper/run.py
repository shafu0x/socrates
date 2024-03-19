from eth_global          import run as get_recipients
from eth_global_disperse import run as get_txs

txs = get_txs()
recipients = []

for i, tx in enumerate(txs): recipients.append(get_recipients(tx))

# flatten the list
recipients = [item for sublist in recipients for item in sublist]

print(recipients)
print(len(recipients))
