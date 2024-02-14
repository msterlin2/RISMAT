import numpy as np

def iFAPlockbox_process(client, iFAPlockbox, market):

    # processes an iFAPlockbox data structure
    # creating a future real annuity with constant payments as long as
    #   anyone is alive

    # compute annual real income per dollar depending on personal state
    # when annuity is purchased
    # find mortality rates in future year (if alive)
    FAPyear = iFAPlockbox.yearOfAnnuityPurchase
    mortP1 = client.mortP1[FAPyear:]
    mortP2 = client.mortP2[FAPyear:]

    # compute probabilities of payment for each initial personal state
    # probability of payment each year if only 1 is alive at outset
    probP1Alive = np.cumprod(1 - mortP1)
    # probability of payment each year if only 2 is alive at outset
    probP2Alive = np.cumprod(1 - mortP2)
    # probability of payment if both alive at outset and payment is made
    #   when either or both are alive
    probBothDead = (1 - probP1Alive) * (1 - probP2Alive)
    # add an initial payment of $1 at the beginning of first year
    probPayment1 = np.concatenate([[1], probP1Alive])
    probPayment2 = np.concatenate([[1], probP2Alive])
    probPayment3 = np.concatenate([[1], 1 - probBothDead])

    # find discounted sum of payments
    n = len(probPayment1)
    dfs = market.rf ** np.arange(n)
    pvs = 1 / dfs
    valuePerDollar1 = np.sum(probPayment1 * pvs)
    valuePerDollar2 = np.sum(probPayment2 * pvs)
    valuePerDollar3 = np.sum(probPayment3 * pvs)

    # find costs of annuities for initial personal states
    valOverCost = iFAPlockbox.annuityValueOverCost
    costPerDollar1 = valuePerDollar1 / valOverCost
    costPerDollar2 = valuePerDollar2 / valOverCost
    costPerDollar3 = valuePerDollar3 / valOverCost

    # create values available to purchase annuity
    tipsProp = iFAPlockbox.proportionInTIPS
    tipsProp = max(0, min(1, tipsProp))
    tipsAmt = tipsProp * iFAPlockbox.investedAmount
    mktAmt = iFAPlockbox.investedAmount - tipsAmt
    mktVals = mktAmt * market.cumRmsM[:, FAPyear]
    tipsVals = tipsAmt * market.cumRfsM[:, FAPyear]
    totVals = mktVals + tipsVals

    # create annuity payments and fees vectors
    nscen, nyrs = client.incomesM.shape
    annPayments = np.zeros(nscen)
    feesV = np.zeros(nscen)

    # Handle personal state 1
    ii = np.where(client.pStatesM[:, FAPyear] == 1)[0]
    annPayments[ii] = totVals[ii] / costPerDollar1
    feesV[ii] = (1 - valOverCost) * totVals[ii]

    # Handle personal state 2
    ii = np.where(client.pStatesM[:, FAPyear] == 2)[0]
    annPayments[ii] = totVals[ii] / costPerDollar2
    feesV[ii] = (1 - valOverCost) * totVals[ii]

    # Handle personal state 3
    ii = np.where(client.pStatesM[:, FAPyear] == 3)[0]
    annPayments[ii] = totVals[ii] / costPerDollar3
    feesV[ii] = (1 - valOverCost) * totVals[ii]

    # create incomes matrix
    incsM = np.zeros((nscen, nyrs))
    # add payments in FAPyear
    incsM[:, FAPyear] = annPayments
    # add payments for years after FAPyear
    for yr in range(FAPyear + 1, nyrs):
        ps = client.pStatesM[:, yr]
        v = (ps > 0) & (ps < 4)
        incsM[:, yr] = v * annPayments

    # create fees matrix
    feesM = np.zeros((nscen, nyrs))
    feesM[:, FAPyear] = feesV

    # find payments to estate before FAPyear
    marketValsM = mktAmt * market.cumRmsM
    tipsValsM = tipsAmt * market.cumRfsM
    totValsM = marketValsM + tipsValsM
    totValsM[:, FAPyear + 1:nyrs] = 0
    estatePaidM = client.pStatesM == 4
    amtsPdM = totValsM * estatePaidM

    # add incomes and amounts paid to client incomes
    client.incomesM += incsM + amtsPdM
    # add fees to client fees
    client.feesM += feesM.astype(int)

    return client
