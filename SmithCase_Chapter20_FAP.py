import numpy as np
import matplotlib.pyplot as plt
from client_create import client_create
from client_process import client_process
from market_create import market_create
from market_process import market_process
from analysis_create import analysis_create
from analysis_process import analysis_process 
from AMDnLockboxes_create import AMDnLockboxes_create
from AMDnLockboxes_process import AMDnLockboxes_process
from iLBSplusFAP_create import iLBSplusFAP_create
from iLBSplusFAP_process import iLBSplusFAP_process

# SmithCase_Chapter20_FAP.py

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

# Create AMD2 lockboxes
AMDnLockboxes = AMDnLockboxes_create()
AMDnLockboxes.showProportions = 'y'
AMDnLockboxes = AMDnLockboxes_process(AMDnLockboxes, market, client)

# Create iLBSplusFAP
iLBSplusFAP = iLBSplusFAP_create()
iLBSplusFAP.lockboxProportions = AMDnLockboxes.proportions

# Set proportions in FAP lockbox to those in the last spending lockbox
yr = iLBSplusFAP.annuitizationYear
props = iLBSplusFAP.lockboxProportions[:, yr - 1]
iLBSplusFAP.FAPlockboxProportionInTIPS = props[0] / (props[0] + props[1])

# Process iLBSplusFAP
client, iLBSplusFAP = iLBSplusFAP_process(client, iLBSplusFAP, market)

# Create analysis
analysis = analysis_create()

analysis.plotScenarios = 'y'
analysis.plotScenariosTypes = ['ri']
analysis.plotScenariosNumber = 20

analysis.plotIncomeDistributions = 'y'
analysis.plotIncomeDistributionsTypes = ['rc']
analysis.plotIncomeDistributionsStates = [[3, 1, 2]]
analysis.plotIncomeDistributionsMinPctScenarios = 0.5
analysis.plotIncomeDistributionsPctMaxIncome = 50

analysis.plotYearlyPVs = 'y'
analysis.plotYearlyPVsStates = [[3, 1, 2]]

analysis.plotRecipientPVs = 'y'

# Process analysis
analysis_process(analysis, client, market)
