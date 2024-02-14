import numpy as np

# INPUTS
EOQmarketCaps = np.array([[17.04, 16.83], [22.59, 18.80]])
EOQprices = np.array([[10.72, 20.90], [52.10, 30.20]])
currentPrices = np.array([[10.69, 20.88], [52.40, 30.08]])
amountInvested = 100000

# COMPUTATIONS
EOQproportions = EOQmarketCaps / np.sum(np.sum(EOQmarketCaps))
priceRatios = currentPrices / EOQprices
products = EOQproportions * priceRatios
revisedProportions = products / np.sum(np.sum(products))
desiredValues = revisedProportions * amountInvested
trades = np.round(desiredValues)

# SHOW RESULTS
print("Dollar amounts to be traded:")
print(trades)
