import numpy as np
from iFixedAnnuity_create import iFixedAnnuity_create
from iFixedAnnuity_process import iFixedAnnuity_process
from iLockboxSpending_create import iLockboxSpending_create
from iLockboxSpending_process import iLockboxSpending_process
import copy



'''
class iLBSplusDFA:
    def __init__(self):
        

        # lockbox proportions (matrix with TIPS in top row, market in bottom row)
        self.lockboxProportions = []

        # number of years of lockbox income
        self.numberOfLockboxYears = 20

        # lockbox bequest utility ratio
        self.bequestUtilityRatio = 0.50

        # percentile of last lockbox year income distribution for fixed annuity
        # 100=lowest income; 50=median income, 0=highest income
        self.percentileOfLastLockboxYear = 50

        # fixed annuity ratio of value to initial cost
        self.annuityValueOverCost = 0.90

        # total amount invested
        self.amountInvested = 100000

        # Amounts invested in lockbox and deferred annuity
        self.DFAInvestment = 0
        self.LBInvestment = 0

'''
def iLBSplusDFA_process(client, iLBSplusDFA, market):
    # process lockbox spending plus deferred fixed annuity

    # Create deferred fixed annuity with cost equal to 50% of total
    iFixedAnnuity = iFixedAnnuity_create()
    # Set deferral period
    nLByrs = iLBSplusDFA.numberOfLockboxYears
    iFixedAnnuity.guaranteedIncomes = np.zeros(nLByrs)
    # Set relative incomes equal for personal states 1,2, and 3
    iFixedAnnuity.pStateIncomes = [0, 1, 1, 1, 0]
    # Set incomes constant
    iFixedAnnuity.graduationRatio = 1.00
    # Set type of income to real
    iFixedAnnuity.realOrNominal = 'r'
    # Set ratio of value to initial cost
    iFixedAnnuity.valueOverCost = iLBSplusDFA.annuityValueOverCost
    # Cost
    iFixedAnnuity.cost = 0.50 * iLBSplusDFA.amountInvested
    # Create a temporary client with zero incomes
    clientTemp = copy.copy(client)
    clientTemp.incomesM = np.zeros_like(clientTemp.incomesM)
    # Process deferred fixed annuity with temporary client
    clientTemp = iFixedAnnuity_process(iFixedAnnuity, clientTemp, market)
    # Find annuity real income per dollar invested
    annuityIncomePerDollar = np.max(np.max(clientTemp.incomesM)) / iFixedAnnuity.cost

    # Create lockbox spending with cost equal to 50% of total
    iLockboxSpending = iLockboxSpending_create()
    # Set lockbox proportions for the selected number of years
    props = iLBSplusDFA.lockboxProportions[:, :nLByrs]
    iLockboxSpending.lockboxProportions = props
    # Set initial investment
    iLockboxSpending.investedAmount = 0.50 * iLBSplusDFA.amountInvested
    # Bequest utility ratio
    iLockboxSpending.bequestUtilityRatio = iLBSplusDFA.bequestUtilityRatio
    # Show lockbox amounts (y or n)
    iLockboxSpending.showLockboxAmounts = 'n'
    # Create a new temporary client with zero incomes
    clientTemp = copy.copy(client)
    clientTemp.incomesM = np.zeros_like(clientTemp.incomesM)
    # Process lockbox spending with a temporary client
    clientTemp, iLockboxSpending = iLockboxSpending_process(iLockboxSpending, clientTemp, market)
    # Find incomes in the final year per dollar invested
    pstates = clientTemp.pStatesM[:, nLByrs - 1]
    ii = np.where((pstates > 0) & (pstates < 4))[0]
    incs = np.sort(clientTemp.incomesM[ii, nLByrs - 1])[::-1]
    incsPerDollar = incs / iLockboxSpending.investedAmount
    numIncsPerDollar = len(incsPerDollar)
    # Find the percentile of income in the final year per dollar invested
    pctl = iLBSplusDFA.percentileOfLastLockboxYear
    incNum = int(round(0.01 * pctl * numIncsPerDollar))
    incNum = max(1, incNum)
    incNum = min(numIncsPerDollar, incNum)
    LBIncomePerDollar = incsPerDollar[incNum - 1]

    # Find amounts to invest in lockbox and deferred annuity
    r = annuityIncomePerDollar / (LBIncomePerDollar + annuityIncomePerDollar)
    LBInvestment = r * iLBSplusDFA.amountInvested
    DFAInvestment = iLBSplusDFA.amountInvested - LBInvestment

    # Create incomes from deferred fixed annuity
    clientTemp = copy.copy(client)
    iFixedAnnuity.cost = DFAInvestment
    clientTemp = iFixedAnnuity_process(iFixedAnnuity, clientTemp, market)
    DFAincsM = clientTemp.incomesM
    feesM = clientTemp.feesM

    # Create incomes from lockbox spending
    clientTemp = copy.copy(client)
    clientTemp.incomesM = np.zeros_like(clientTemp.incomesM)
    iLockboxSpending.investedAmount = LBInvestment
    clientTemp, iLockboxSpending = iLockboxSpending_process(iLockboxSpending, clientTemp, market)
    LBincsM = clientTemp.incomesM

    # Add amounts invested to iLBSplusDFA data structure
    iLBSplusDFA.DFAInvestment = DFAInvestment
    iLBSplusDFA.LBInvestment = LBInvestment

    # Add incomes to the client income matrix
    client.incomesM = client.incomesM + DFAincsM + LBincsM
    client.feesM = client.feesM + feesM

    return client, iLBSplusDFA
