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

# SmithCase_Chapter13.py

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

# Plot recipient present values -- y (yes) or n (no)
analysis.plotRecipientPVs = 'y'

# Plot PPCs and Incomes -- y/n
analysis.plotPPCSandIncomes = 'y'
# Plot PPC and Incomes -- semilog or loglog
analysis.plotPPCSandIncomesSemilog = 'y'
# Plot PPCs and Incomes -- sets of states (one set per graph)
analysis.plotPPCSandIncomesStates = [[3]]
# Plot PPCs and Incomes: minimum percent of scenarios
analysis.plotPPCSandIncomesMinPctScenarios = 0.5

# Plot yearly present values -- y (yes) or n (no)
analysis.plotYearlyPVs = 'y'
# Plot yearly present values-- sets of states (one set per graph)
analysis.plotYearlyPVsStates = [[3], [1, 2]]
# Plot yearly present values: minimum percent of scenarios
analysis.plotYearlyPVsMinPctScenarios = 0.5

# Plot efficient incomes -- y (yes) or n (no)
analysis.plotEfficientIncomes = 'y'
# Plot efficient incomes -- sets of states (one set per graph)
analysis.plotEfficientIncomesStates = [[3]]
# Plot points (actual) curves (efficient) and/or
#   lines (two-asset market-based strategies
#   combinations of (p,c,l) -- one graph per type
analysis.plotEfficientIncomesTypes = ['pcl']
# Plot efficient incomes: minimum percent of scenarios
analysis.plotEfficientIncomesMinPctScenarios = 0.5

# Process analysis
analysis_process(analysis, client, market)
