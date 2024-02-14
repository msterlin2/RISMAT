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
from iConstSpending_create import iConstSpending_create
from iConstSpending_process import iConstSpending_process


# SmithCase_Chapter17.py

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

# Create social security accounts
iSocialSecurity = iSocialSecurity_create()
iSocialSecurity.state1Incomes = [float('inf'), 30000]
iSocialSecurity.state2Incomes = [float('inf'), 30000]
iSocialSecurity.state3Incomes = [44000]
# Process social security accounts
client = iSocialSecurity_process(iSocialSecurity, client, market)

# Create constant spending data structure
iConstSpending = iConstSpending_create()
iConstSpending.glidePath = np.array([[1.0],[1.0]])
iConstSpending.retentionRatio = 0.999
iConstSpending.initialProportionSpent = 0.040
iConstSpending.graduationRatio = 1.00
iConstSpending.pStateRelativeIncomes = [1, 1, 1]
iConstSpending.investedAmount = 1000000
iConstSpending.showGlidePath = 'y'
# Process the constant spending data structure
client = iConstSpending_process(iConstSpending, client, market)

# Create analysis
analysis = analysis_create()

# Reset analysis parameters
analysis.animationDelays = [0.5, 0.5]
analysis.animationShadowShade = 1

analysis.figuresCloseWhenDone = 'n'
analysis.stackFigures = 'y'
analysis.figureDelay = 0

analysis.plotScenarios = 'y'
analysis.plotScenariosTypes = ['ri']
analysis.plotScenariosNumber = 20

analysis.plotRecipientPVs = 'y'

analysis.plotYearlyPVs = 'y'
analysis.plotYearlyPVsStates = [[1, 2], [3]]

# Produce analysis
analysis_process(analysis, client, market)