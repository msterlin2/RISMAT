import numpy as np

def iLBAnnuity_process(iLBAnnuity, client, market):
    # creates LB annuity income matrix and fees matrix
    # then adds values to client incomes matrix and fees matrices

    # the lockbox proportions matrix can be computed by AMDnLockboxes_process
    # or in some other manner. The first row is TIPS proportions, the second is Market
    # proportions, and there is a column for each year in the client matrix

    # get number of scenarios and years
    nscen, nyrs = client.pStatesM.shape

    # set initial lockbox proportions
    proportions = np.array(iLBAnnuity.proportions)

    # reset proportions to adjust for graduation and retention ratios
    gr = iLBAnnuity.graduationRatio
    rrs = iLBAnnuity.retentionRatios
    for row in range(2):
        factors = (gr / rrs[row]) ** np.arange(nyrs)
        proportions[row, :] = factors * proportions[row, :]
    
    # set lockbox proportions to zero for any excluded years
    firstyear = iLBAnnuity.firstIncomeYear
    if firstyear > 1:
        proportions[:, :firstyear-1] = np.zeros((2, firstyear-1))

    # create matrices of returns net of expenses
    NrfsM = iLBAnnuity.retentionRatios[0] * market.rfsM
    NrmsM = iLBAnnuity.retentionRatios[1] * market.rmsM

    # Create matrices of cumulative returns net of expenses
    m = np.cumprod(NrfsM, axis=1)
    cumNrfsM = np.hstack([np.ones((nscen, 1)), m[:, :nyrs-1]])

    m = np.cumprod(NrmsM, axis=1)
    cumNrmsM = np.hstack([np.ones((nscen, 1)), m[:, :nyrs-1]])
    
    # create matrices with proportions in market and rf in each row
    xfm = np.ones((nscen, 1)) * proportions[0, :]
    xmm = np.ones((nscen, 1)) * proportions[1, :]

    # compute net incomes for lockbox relative proportions
    boxIncsM = xfm * cumNrfsM + xmm * cumNrmsM
    
    # compute incomes if there were no expenses
    gboxIncsM = xfm * market.cumRfsM + xmm * market.cumRmsM
    
    # set fees to differences
    feesM = gboxIncsM - boxIncsM

    # set up relative incomes matrix and relative fees matrix
    psRelIncs = iLBAnnuity.pStateRelativeIncomes
    psRelIncs = np.array(psRelIncs)
    psRelIncs = psRelIncs / max(psRelIncs)

    relIncsM = np.zeros((nscen, nyrs))
    relFeesM = np.zeros((nscen, nyrs))

    for ps in range(0, 5):
        relInc = psRelIncs[ps - 1] 
        psmat = (client.pStatesM == ps) 
        psIncsM = relInc * (psmat * boxIncsM) 
        relIncsM += psIncsM
        psFeesM = relInc * (psmat * feesM)
        relFeesM += psFeesM
        
    # convert relative incomes to dollar incomes
    pvbase = np.sum(np.sum((relIncsM + relFeesM) * market.pvsM))
    totval = iLBAnnuity.cost * iLBAnnuity.valueOverCost
    incsM = relIncsM * (totval / pvbase)
    feesM = relFeesM * (totval / pvbase)

    # add incomes and fees to client incomes and fees matrices
    client.incomesM += incsM 
    client.feesM = client.feesM.astype(float)  # MS- Convert to float
    feesM = feesM.astype(float)  # MS - Convert to float
    client.feesM += feesM

    # add insurance fee to fee matrix
    insFee = iLBAnnuity.cost * (1 - iLBAnnuity.valueOverCost)
    client.feesM[:, 0] += insFee

    return client
