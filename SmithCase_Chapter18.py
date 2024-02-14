import numpy as np
import matplotlib.pyplot as plt
from client_create import client_create
from client_process import client_process
from market_create import market_create
from market_process import market_process
from analysis_create import analysis_create
from analysis_process import analysis_process
from iPropSpending_create import iPropSpending_create
from iPropSpending_process import iPropSpending_process

# SmithCase_Chapter18.py

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

# Create proportional spending account
iPropSpending = iPropSpending_create()
iPropSpending.investedAmount = 1000000
iPropSpending.glidePath = [[1, 0], [0, 30]]
iPropSpending.showGlidePath = 'y'
iPropSpending.retentionRatio = 0.999
# Process proportional spending account
client = iPropSpending_process(iPropSpending, client, market)

# Create analysis
analysis = analysis_create()

# Change selected analysis settings
analysis.animationDelays = [0.2, 0.2]

analysis.plotIncomeDistributions = 'y'
analysis.plotIncomeDistributionsTypes = ['rc']
analysis.plotIncomeDistributionsStates = [[1, 2, 3]]
analysis.plotIncomeDistributionsMinPctScenarios = 0.5

analysis.plotYOYIncomes = 'y'
analysis.plotYOYIncomesTypes = ['r']
analysis.plotYOYIncomesStates = [[3, 1, 2]]

analysis.plotScenarios = 'y'
analysis.plotScenariosTypes = ['ri']
analysis.plotScenariosNumber = 20

analysis.plotRecipientPVs = 'y'

analysis.plotIncomeMaps = 'y'
analysis.plotIncomeMapsTypes = ['ru', 'rc']
analysis.plotIncomeMapsStates = [[3, 1, 2]]
analysis.plotIncomeMapsMinPctScenarios = 0.5

analysis.plotPPCSandIncomes = 'y'
analysis.plotPPCSandIncomesSemilog = 'y'
analysis.plotPPCSandIncomesStates = [[3, 1, 2]]

analysis.plotYearlyPVs = 'y'
analysis.plotYearlyPVsStates = [[3, 1, 2]]

# Process analysis
analysis_process(analysis, client, market)
