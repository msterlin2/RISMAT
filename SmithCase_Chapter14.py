import numpy as np
import matplotlib.pyplot as plt
from client_create import client_create
from client_process import client_process
from market_create import market_create
from market_process import market_process
from analysis_create import analysis_create
from analysis_process import analysis_process 
from iSocialSecurity_create import iSocialSecurity_create
from iSocialSecurity_process import iSocialSecurity_process


# SmithCase_Chapter14.py

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

# Create social security
iSocialSecurity = iSocialSecurity_create()
# Incomes in state 1, last column repeated for subsequent years
iSocialSecurity.state1Incomes = [float('inf'), 30000]
# Incomes in state 2, last column repeated for subsequent years
iSocialSecurity.state2Incomes = [float('inf'), 30000]
# Incomes for state 3, last column repeated for subsequent years
iSocialSecurity.state3Incomes = [44000]
# Process social security
client = iSocialSecurity_process(iSocialSecurity, client, market)

# Create analysis
analysis = analysis_create()
analysis.plotRecipientPVs = 'y'
# Process analysis
analysis_process(analysis, client, market)
