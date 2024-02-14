import numpy as np

def iGLWB_process(client, market, iGLWB):
    # set parameters
    initialValue = iGLWB.initialValue
    expPropTWB = iGLWB.expenseRatioOfTWB
    expPropFund = iGLWB.expenseRatioOfFund

    # find proportion of TWB to withdraw
    minAge = min(client.p1Age, client.p2Age)
    tbl = iGLWB.jointLifeWithdrawalRates if iGLWB.singleOrJoint.lower() == 'j' else iGLWB.singleLifeWithdrawalRates
    tbl = np.asarray(tbl)
    rows = (minAge >= tbl[:, 0]) & (minAge <= tbl[:, 1])
    withdrawPropTWB = np.sum(rows * tbl[:, 2])

    # create matrix of nominal market returns
    nrmsM = market.rmsM * market.csM

    # get matrix dimensions
    nscen, nyrs = client.incomesM.shape

    # set initial portfolio value vector
    portvalV = initialValue * np.ones(nscen)
    # set vector of total withdrawal bases
    twbV = portvalV.copy()

    # create nominal incomes and nominal fees matrices
    incsM = np.zeros((nscen, nyrs))
    feesFundM = np.zeros((nscen, nyrs))
    feesRiderM = np.zeros((nscen, nyrs))

    # set initial year payouts
    incsM[:, 0] = withdrawPropTWB * twbV
    # adjust portfolio values
    portvalV -= incsM[:, 0]
    # set initial year fees to zero
    feesFundM[:, 0] = np.zeros(nscen)
    feesRiderM[:, 0] = np.zeros(nscen)

    # do remaining years
    for yr in range(1, nyrs):
        # find scenarios in which one or two are alive
        ii = np.where((client.pStatesM[:, yr] > 0) & (client.pStatesM[:, yr] < 4))[0]
        if len(ii) > 0:
            # increment nominal values of portfolio
            portvalV[ii] *= nrmsM[ii, yr - 1]
            # compute fees for fund and subtract from portfolio value
            feesFundM[ii, yr] = expPropFund * portvalV[ii]
            portvalV[ii] -= feesFundM[ii, yr]
            # compute guaranteed withdrawals and add to incomes
            incsM[ii, yr] = withdrawPropTWB * twbV[ii]
            # subtract withdrawals from portfolio values
            portvalV[ii] -= incsM[ii, yr]
            # compute rider fees
            feesRiderM[ii, yr] = expPropTWB * twbV[ii]
            # subtract rider fees from portfolio values
            portvalV[ii] -= feesRiderM[ii, yr]
            # for negative portfolio values, adjust rider fees
            negvalV = np.zeros(nscen)
            negvalV[ii] = np.minimum(portvalV[ii], 0)
            feesRiderM[ii, yr] += negvalV[ii]
            portvalV[ii] -= negvalV[ii]
            # set TWB values to max of portfolio values and prior TWB
            twbV[ii] = np.maximum(portvalV[ii], twbV[ii])

        # scenarios in which estate is paid
        ii = np.where(client.pStatesM[:, yr] == 4)[0]
        if len(ii) > 0:
            # increment nominal values of portfolio
            portvalV[ii] *= nrmsM[ii, yr - 1]
            # compute fees for fund and subtract from portfolio value
            feesFundM[ii, yr] = expPropFund * portvalV[ii]
            portvalV[ii] -= feesFundM[ii, yr]
            # pay remaining portfolio value to estate
            incsM[ii, yr] = portvalV[ii]
            #portvalV[ii] -= incsM[ii]
            portvalV[ii] -= np.sum(incsM[ii], axis=1) 

    # convert nominal incomes matrix to real
    rincsM = incsM / market.cumCsM
    # convert nominal fees matrices to real fees
    rfeesRiderM = feesRiderM / market.cumCsM
    rfeesFundM = feesFundM / market.cumCsM
    # add results to client income and fee matrices
    client.incomesM = client.incomesM.astype('float64') + rincsM 
    client.feesM = client.feesM.astype('float64') + rfeesRiderM + rfeesFundM 

    # if desired add matrices of fees to iGLWB data structure
    if iGLWB.saveFeeMatrices.lower() == 'y':
        iGLWB.feesRiderM = rfeesRiderM
        iGLWB.feesFundM = rfeesFundM

    return client, iGLWB