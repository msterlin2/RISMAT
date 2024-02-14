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
from iLBSplusDFA_create import iLBSplusDFA_create
from iLBSplusDFA_process import iLBSplusDFA_process

# SmithCase_Chapter20_DFA.py

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

# Create iLockboxSpending plus deferred fixed annuity
iLBSplusDFA = iLBSplusDFA_create()
iLBSplusDFA.numberOfLockboxYears = 20
iLBSplusDFA.bequestUtilityRatio = 0.50
iLBSplusDFA.percentileOfLastLockboxYear = 50
iLBSplusDFA.annuityValueOverCost = 0.90
iLBSplusDFA.amountInvested = 1000000

# Set lockbox proportions
iLBSplusDFA.lockboxProportions = AMDnLockboxes.proportions

# Process LockboxSpending
client, iLBSplusDFA = iLBSplusDFA_process(client, iLBSplusDFA, market)

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

analysis.plotRecipientPVs = 'n'

analysis.plotYearlyPVs = 'y'
analysis.plotYearlyPVsStates = [[3, 1, 2]]

analysis.plotRecipientPVs = 'y'

# Process analysis
analysis_process(analysis, client, market)
