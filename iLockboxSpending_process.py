import numpy as np
import matplotlib.pyplot as plt

#MS - adding function to deal with divide by zero error in survanyone log calc 
def safe_log(x, eps=1e-10):
    return np.log(x + eps)

def iLockboxSpending_process(iLockboxSpending, client, market):
    # creates LB spending income matrix and fees matrix
    # then adds values to client incomes matrix and fees matrices
  
    # the lockbox proportions matrix can be computed by AMDnLockboxes_process
    #   or in some other manner. The first row is TIPS, the second is Market
    #   proportions, and there is a column for each year in the client matrix

    # Get the number of scenarios and years
    nscen, nyrs = client.pStatesM.shape

    # Fill lockbox proportions with zeros if needed
    props = iLockboxSpending.lockboxProportions
    nlbyears = props.shape[1]
    props = np.concatenate([props[:, :nlbyears], np.zeros((2, nyrs - nlbyears))], axis=1)
    if props.shape[1] > nyrs:
        props = props[:, :nyrs]

    # Compute survival rates
    surv1 = np.cumprod(1 - client.mortP1)
    surv2 = np.cumprod(1 - client.mortP2)
    survboth = surv1 * surv2
    surv1only = surv1 * (1 - surv2)
    surv2only = surv2 * (1 - surv1)
    survanyone = survboth + surv1only + surv2only
  
    # Adjust proportions to take bequest utility ratio into account
    #ranyoneV = np.exp(np.log(survanyone) / market.b)
    ranyoneV = np.exp(safe_log(survanyone) / market.b)
    rmaxV = np.ones(nyrs)
    bur = iLockboxSpending.bequestUtilityRatio
    ratioV = bur * rmaxV + (1 - bur) * ranyoneV

    # Change market proportions to keep the total the same
    oldsum = np.sum(props[1, :])
    newmktprops = ratioV * props[1, :]
    newsum = np.sum(newmktprops)
    newmktprops = (newmktprops / newsum) * oldsum
    newprops = np.vstack([props[0, :], newmktprops])

    # Save new proportions
    iLockboxSpending.adjustedLockboxProportions = newprops

    # Compute lockbox dollar values
    #LBVals = (newprops / np.sum(np.sum(newprops))) * iLockboxSpending.investedAmount
    LBVals = (newprops / np.sum(newprops)) * iLockboxSpending.investedAmount

    # Plot lockbox amounts if requested
    if iLockboxSpending.showLockboxAmounts.lower() == 'y':
        xs = LBVals
        fig, ax = plt.subplots()
        x = np.arange(1, xs.shape[1] + 1)
        ax.bar(x, xs[0, :], label='TIPS')
        ax.bar(x, xs[1, :], label='Market', bottom=xs[0, :])
        ax.grid(True)
        ax.set_xlabel('Lockbox Maturity Year')
        ax.set_ylabel('Amount Invested at Inception')
        ax.legend()
        plt.show()

    # Create incomes
    incsM = np.zeros((nscen, nyrs))
    for yr in range(nyrs):
        # Scenarios with anyone alive
        ii = np.where((client.pStatesM[:, yr] > 0) & (client.pStatesM[:, yr] < 4))[0]
        # Add cumulative value of tips
        incsM[ii, yr] = LBVals[0, yr] * market.cumRfsM[ii, yr]
        # Add cumulative value of market
        incsM[ii, yr] += LBVals[1, yr] * market.cumRmsM[ii, yr]

        # Scenarios with estate
        ii = np.where(client.pStatesM[:, yr] == 4)[0]
        # Values of current and remaining lockboxes
        m = np.sum(LBVals[:, yr:nyrs], axis=1)
        # Add cumulative values of tips
        incsM[ii, yr] = m[0] * market.cumRfsM[ii, yr]
        # Add cumulative value of market
        incsM[ii, yr] += m[1] * market.cumRmsM[ii, yr]

    # Add incomes to client incomes matrix
    client.incomesM += incsM.astype(int)

    return client, iLockboxSpending
