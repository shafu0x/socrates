from eth_global          import run as eth_global
from eth_global_disperse import run as eth_global_disperse

txs = eth_global_disperse()
recipients = []

for i, tx in enumerate(txs):
    print(i)
    recipients.append(eth_global(tx))
    if i == 2: break

# flatten the list
recipients = [item for sublist in recipients for item in sublist]
print(len(recipients))
