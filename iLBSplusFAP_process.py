import numpy as np
from iLockboxSpending_create import iLockboxSpending_create
from iLockboxSpending_process import iLockboxSpending_process
from iFAPlockbox_create import iFAPlockbox_create
from iFAPlockbox_process import iFAPlockbox_process
import copy


def iLBSplusFAP_process(client, iLBSplusFAP, market):
    # process lockbox spending plus deferred fixed annuity 

    # Create a temporary client
    clientTemp = copy.copy(client)

    # Process lockbox spending with 0.5 of the total amount invested
    iLockboxSpending = iLockboxSpending_create()

    # Set lockbox proportions
    iLockboxSpending.lockboxProportions = iLBSplusFAP.lockboxProportions

    # Use lockbox spending up to and including the year before annuity purchase
    lastSpendingYr = iLBSplusFAP.annuitizationYear - 1
    iLockboxSpending.lockboxProportions = iLockboxSpending.lockboxProportions[:, :lastSpendingYr]

    # Set bequest utility ratio
    iLockboxSpending.bequestUtilityRatio = iLBSplusFAP.bequestUtilityRatio

    # Do not show lockbox proportions
    iLockboxSpending.showLockboxAmounts = 'n'

    # Amount invested for lockbox spending
    iLockboxSpending.investedAmount = 0.50 * iLBSplusFAP.amountInvested

    # Process lockbox spending
    clientTemp = copy.copy(client)
    nscen, nyrs = client.incomesM.shape
    clientTemp.incomesM = np.zeros((nscen, nyrs))
    clientTemp, _ = iLockboxSpending_process(iLockboxSpending, clientTemp, market)

    # Find percentile income in the last lockbox spending year for matching states
    ps = clientTemp.pStatesM[:, lastSpendingYr]
    ii = np.where((ps > 0) & (ps < 4))[0]
    incs = clientTemp.incomesM[ii, lastSpendingYr]
    sortincs = np.sort(incs)[::-1]
    matchPctl = iLBSplusFAP.incomePercentileToMatch / 100
    matchPctl = min(max(matchPctl, 0), 1)
    n = int(round(matchPctl * len(sortincs)))
    n = min(max(n, 1), len(sortincs))
    pctlIncSpending = sortincs[n - 1]

    # Create lockbox for future annuity purchase
    iFAPlockbox = iFAPlockbox_create()

    # Set the year the annuity is to be purchased
    iFAPlockbox.yearOfAnnuityPurchase = iLBSplusFAP.annuitizationYear

    # Set initial proportion in TIPS in the FAP lockbox
    propTIPS = iLBSplusFAP.FAPlockboxProportionInTIPS
    iFAPlockbox.proportionInTIPS = propTIPS

    # Set the initial amount ($) in the lockbox
    iFAPlockbox.investedAmount = 0.50 * iLBSplusFAP.amountInvested

    # Process FAP lockbox with a temporary client
    clientTemp = copy.copy(client)
    clientTemp.incomesM = np.zeros((nscen, nyrs))
    clientTemp = iFAPlockbox_process(clientTemp, iFAPlockbox, market)

    # Find percentile amount spent in the first annuity year matching states
    ps = clientTemp.pStatesM[:, lastSpendingYr + 1]
    incs = clientTemp.incomesM[ii, lastSpendingYr + 1]
    sortincs = np.sort(incs)[::-1]
    n = int(round(matchPctl * len(sortincs)))
    n = min(max(n, 1), len(sortincs))
    pctlIncAnnuity = sortincs[n - 1]

    # Compute revised amounts to be invested
    # Find incomes per dollar
    incomePerDollarSpending = pctlIncSpending / iLockboxSpending.investedAmount
    incomePerDollarAnnuity = pctlIncAnnuity / iFAPlockbox.investedAmount

    # Find proportions of total investment
    sum_income = incomePerDollarSpending + incomePerDollarAnnuity
    propSpending = incomePerDollarAnnuity / sum_income
    propAnnuity = incomePerDollarSpending / sum_income

    # Find the total amount invested
    totAmountInvested = iLockboxSpending.investedAmount + iFAPlockbox.investedAmount

    # Put amounts to be invested in data structures
    iLockboxSpending.investedAmount = propSpending * totAmountInvested
    iFAPlockbox.investedAmount = propAnnuity * totAmountInvested

    # Add to iLBSplusFAP data structure
    iLBSplusFAP.spendingAmountInvested = iLockboxSpending.investedAmount
    iLBSplusFAP.FAPAmountInvested = iFAPlockbox.investedAmount

    # Create incomes from lockbox spending
    clientTemp = client
    clientTemp.incomesM = np.zeros((nscen, nyrs))
    clientTemp, _ = iLockboxSpending_process(iLockboxSpending, clientTemp, market)

    # Add incomes and fees from FAP
    clientTemp = iFAPlockbox_process(clientTemp, iFAPlockbox, market)

    # Add incomes to the client income matrix
    client.incomesM = client.incomesM + clientTemp.incomesM

    # Add fees to the client fee matrix
    client.feesM = client.feesM + clientTemp.feesM

    return client, iLBSplusFAP
