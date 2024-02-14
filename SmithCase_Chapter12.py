import numpy as np
import matplotlib.pyplot as plt
from client_create import client_create
from client_process import client_process
from market_create import market_create
from market_process import market_process
from iFixedAnnuity_create import iFixedAnnuity_create
from iFixedAnnuity_process import iFixedAnnuity_process
from analysis_create import analysis_create
from analysis_process import analysis_process

# SmithCase_Chapter12.py

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

# Create fixed nominal Annuity
iFixedAnnuity = iFixedAnnuity_create()
iFixedAnnuity.realOrNominal = 'n'
# Process fixed annuity
client = iFixedAnnuity_process(iFixedAnnuity, client, market)

# Create analysis
analysis = analysis_create()

# Plot scenarios
analysis.plotScenarios = 'y'
analysis.plotScenariosTypes = ['rie']
analysis.plotScenariosNumber = 10

# Plot income distributions
analysis.plotIncomeDistributions = 'y'
analysis.plotIncomeDistributionsTypes = ['rc', 'ru']
analysis.plotIncomeDistributionsStates = [[3]]
analysis.plotIncomeDistributionsMinPctScenarios = 0.5

# Plot income maps
analysis.plotIncomeMaps = 'y'
analysis.plotIncomeMapsTypes = ['ru', 'rc']
analysis.plotIncomeMapsStates = [[3]]
analysis.plotIncomeMapsMinPctScenarios = 0.5

# Plot year-over-year incomes
analysis.plotYOYIncomes = 'y'
analysis.plotYOYIncomesTypes = ['r']
analysis.plotYOYIncomesStates = [[3]]

# Process analysis
analysis_process(analysis, client, market)
