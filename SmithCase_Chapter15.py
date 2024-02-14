import numpy as np
import matplotlib.pyplot as plt
from client_create import client_create
from client_process import client_process
from market_create import market_create
from market_process import market_process
from AMDnLockboxes_create import AMDnLockboxes_create
from AMDnLockboxes_process import AMDnLockboxes_process
from CMULockboxes_create import CMULockboxes_create
from CMULockboxes_process import CMULockboxes_process
from combinedLockboxes_create import combinedLockboxes_create
from combinedLockboxes_process import  combinedLockboxes_process

# SmithCase_Chapter15.py

# Clear all previous variables and close any figures
plt.close('all')

# Create a new client data structure
client = client_create()
# Process the client data structure
client = client_process(client)

# Create a new market data structure
market = market_create()
# Process the client data structure
market = market_process(market, client)

# Create and process AMDnLockboxes
AMDnLockboxes = AMDnLockboxes_create()
AMDnLockboxes.showProportions = 'y'
AMDnLockboxes = AMDnLockboxes_process(AMDnLockboxes, market, client)

# Create and process CMULockboxes
CMULockboxes = CMULockboxes_create()
CMULockboxes.showProportions = 'y'
CMULockboxes = CMULockboxes_process(CMULockboxes, market, client)

# Create and process combined lockboxes
combinedLockboxes = combinedLockboxes_create()
combinedLockboxes.componentLockboxes = [AMDnLockboxes, CMULockboxes]
combinedLockboxes.componentWeights = [0.5, 0.5]
combinedLockboxes.showCombinedProportions = 'y'
combinedLockboxes = combinedLockboxes_process(combinedLockboxes, market, client)
