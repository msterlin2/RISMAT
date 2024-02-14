import numpy as np

def iFixedAnnuity_process(iFixedAnnuity, client, market):
    # creates fixed annuity income matrix and fees matrix
    # then adds values to client incomes matrix and fees matricesco
    
    # get the number of scenarios and years
    nscen, nyrs = client.pStatesM.shape

    # make a matrix of incomes for states 0,1,2,3, and 4
    psIncomesM = np.empty((0, nyrs))
    for pState in range(5):
        # guaranteed incomes
        if pState == 0:
            guarIncomes = np.zeros_like(iFixedAnnuity.guaranteedIncomes)
        elif 0 < pState < 4:
            guarIncomes = iFixedAnnuity.guaranteedIncomes
        else:
            guarIncomes = np.flip(np.cumsum(iFixedAnnuity.guaranteedIncomes))

        # annuity incomes
        nAnnYrs = nyrs - len(iFixedAnnuity.guaranteedIncomes)
        gradRatios = iFixedAnnuity.graduationRatio ** np.arange(nAnnYrs)
        annIncomes = iFixedAnnuity.pStateIncomes[pState] * gradRatios

        # guaranteed and annuity incomes
        psIncomes = np.concatenate((guarIncomes, annIncomes))

        # add to matrix
        psIncomesM = np.vstack((psIncomesM, psIncomes))

    # create a matrix of relative incomes for all scenarios
    incomesM = np.zeros((nscen, nyrs))
    for pState in range(5):
        # make a matrix of incomes for the personal state
        mat = np.ones((nscen, 1)) * psIncomesM[pState, :]
        # find cells in the client personal state matrix for this state
        ii = np.where(client.pStatesM == pState)
        # put selected incomes in the incomes Matrix
        incomesM[ii] = mat[ii]

    # if values are nominal, change to real
    if iFixedAnnuity.realOrNominal.lower() == 'n':
        incomesM = incomesM / market.cumCsM

    # compute the present value of all relative incomes
    pvIncomes = np.sum(np.sum(incomesM * market.pvsM))

    # create a fee matrix
    feesM = np.zeros((nscen, nyrs))
    # compute the value of the annuity purchased
    annVal = iFixedAnnuity.valueOverCost * iFixedAnnuity.cost
    # add fee to the matrix in column 1
    feesM[:, 0] = iFixedAnnuity.cost - annVal

    # scale incomes so pv = amount invested - fee
    factor = annVal / pvIncomes
    incomesM = incomesM * factor

    # add incomes and fees to client matrices
    client.incomesM = client.incomesM + incomesM
    client.feesM = client.feesM + feesM
    # subtract the cost from the client budget
    client.budget = client.budget - iFixedAnnuity.cost

    return client
