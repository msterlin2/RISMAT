import numpy as np
import matplotlib.pyplot as plt
from client_create import client_create
from client_process import client_process
from market_create import market_create
from market_process import market_process
from analysis_create import analysis_create
from analysis_process import analysis_process 
from iGLWB_create import iGLWB_create
from iGLWB_process import iGLWB_process

# SmithCase_Chapter19.py

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

# Create a new GLWB structure
iGLWB = iGLWB_create()

# Process the GLWB data structure
client, iGLWB = iGLWB_process(client, market, iGLWB)

# Create analysis
analysis = analysis_create()
analysis.animationDelays = [1, 0.5]

# Scenarios
analysis.plotScenarios = 'y'
analysis.plotScenariosTypes = ['ri']
analysis.plotScenariosNumber = 20

analysis.plotIncomeDistributions = 'y'
analysis.plotIncomeDistributionsTypes = ['rc']
analysis.plotIncomeDistributionsStates = [[3, 1, 2]]
analysis.plotIncomeDistributionsMinPctScenarios = 0.5
analysis.plotIncomeDistributionsPctMaxIncome = 50

analysis.plotYOYIncomes = 'n'
analysis.plotYOYIncomesTypes = ['r']
analysis.plotYOYIncomesStates = [[3, 1, 2]]

analysis.plotRecipientPVs = 'y'

analysis.plotIncomeMaps = 'y'
analysis.plotIncomeMapsTypes = ['rc']
analysis.plotIncomeMapsStates = [[3, 1, 2]]
analysis.plotIncomeMapsMinPctScenarios = 0.5
analysis.plotIncomeMapsPctMaxIncome = 25

analysis.plotPPCSandIncomes = 'y'
analysis.plotPPCSandIncomesSemilog = 'y'
analysis.plotPPCSandIncomesStates = [[3, 1, 2]]

analysis.plotYearlyPVs = 'y'
analysis.plotYearlyPVsStates = [[3, 1, 2]]

analysis.plotEfficientIncomes = 'n'
analysis.plotEfficientIncomesStates = [[3, 1, 2]]
analysis.plotEfficientIncomesTypes = ['pcl']

# Process analysis
analysis_process(analysis, client, market)
