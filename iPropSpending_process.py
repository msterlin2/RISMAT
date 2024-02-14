import numpy as np
import matplotlib.pyplot as plt

def iPropSpending_process(iPropSpending, client, market):
    # Get matrix dimensions
    nscen, nyrs = market.rmsM.shape

    # Get glidepath
    path = np.array(iPropSpending.glidePath)

    # Get points from glidepath
    ys, xs = path[0], path[1]

    # Ensure no years prior to 1
    xs = np.maximum(xs, 1)

    # Ensure no market proportions greater than 1 or less than 0
    ys = np.minimum(ys, 1)
    ys = np.maximum(ys, 0)

    # Sort points in increasing order of x values
    ii = np.argsort(xs)
    xs, ys = xs[ii], ys[ii]

    # Add values for year 1 and/or last year if needed
    if xs[0] > 1:
        xs = np.concatenate(([1], xs))
        ys = np.concatenate(([ys[0]], ys))
    if xs[-1] < nyrs:
        xs = np.concatenate((xs, [nyrs]))
        ys = np.concatenate((ys, [ys[-1]]))

    # Create vectors for all years
    pathxs, pathys = [], []
    for i in range(len(xs) - 1):
        xlft, xrt = xs[i], xs[i + 1]
        ylft, yrt = ys[i], ys[i + 1]
        pathxs.extend([xlft, xrt])
        pathys.extend([ylft, yrt])
        if xlft != xrt:
            slope = (yrt - ylft) / (xrt - xlft)
            for x in range(xlft + 1, xrt):
                pathxs.append(x)
                yy = ylft + slope * (x - xlft)
                pathys.append(yy)

    # Show glide path if desired
    if iPropSpending.showGlidePath.lower() == 'y':
        fig, ax = plt.subplots()
        ax.plot(path[1, :], path[0, :], '*b', linewidth=4, label='Input')
        ax.plot(pathxs, pathys, '-r', linewidth=2, label='All')
        ax.legend()
        ax.set(xlabel='Year', ylabel='Proportion in Market Portfolio',
               title='Glide Path: Market Proportions by Year')
        ax.grid()
        plt.show()

    # Create matrix of gross returns for the investment strategy
    retsM = np.zeros((nscen, nyrs))
    for yr in range(nyrs - 1):
        rets = pathys[yr] * market.rmsM[:, yr]
        rets += (1 - pathys[yr]) * market.rfsM[:, yr]
        retsM[:, yr] = rets

    # Get retention ratio
    rr = iPropSpending.retentionRatio

    # Get life expectancies
    if iPropSpending.useRMDlifeExpectancies.lower() == 'y':
        LEs = np.array([27.4, 26.5, 25.6, 24.7, 23.8, 22.9, 22.0, 21.2, 20.3, 19.5, 18.7, 17.9, 17.1,
                        16.3, 15.5, 14.8, 14.1, 13.4, 12.7, 12.0, 11.4, 10.8, 10.2, 9.6, 9.1, 8.6,
                        8.1, 7.6, 7.1, 6.7, 6.3, 5.9, 5.5, 5.2, 4.9, 4.5, 4.2, 3.9, 3.7, 3.4, 3.1,
                        2.9, 2.6, 2.4, 2.1, 1.9])
        firstLEAge = 70
    else:
        # If RMD not used, vector of life expectancies and age for the first value
        LEs = np.array(iPropSpending.nonRMDlifeExpectancies)
        firstAge = iPropSpending.nonRMDfirstLEAge

    # Expand LE vector
    # Assume no mortality before the first age
    firstLE = LEs[0]
    initLEs = firstLE + np.arange(firstLEAge - 1, 0, -1)
    # Assume life expectancy constant after the last age
    LEs = np.concatenate((initLEs, LEs, np.full(120, LEs[-1])))
    # Set life expectancies for years based on the owner's current age
    currAge = iPropSpending.portfolioOwnerCurrentAge
    LEs = LEs[currAge:currAge + nyrs]

    # Find spending proportions and ensure they are between 0 and 1 inclusive
    spendProps = 1.0 / LEs
    spendProps = np.maximum(spendProps, 0)
    spendProps = np.minimum(spendProps, 1)

    # If desired, show proportions spent
    if iPropSpending.showProportionsSpent.lower() == 'y':
        fig2, ax2 = plt.subplots()
        xs = np.arange(1, nyrs + 1)
        ys = spendProps
        ax2.plot(xs, ys, '*r-', linewidth=2)
        ax2.set(xlabel='Year', ylabel='Proportion of Portfolio Value Spent',
                title='Proportions of Portfolio Spent')
        ax2.grid()
        plt.show()

    # If desired, show Lockbox Equivalent Values
    if iPropSpending.showLockboxEquivalentValues.lower() == 'y':
        # Find lockbox equivalent values
        facs = 1 - spendProps
        facs = np.concatenate(([1], facs))
        lbVals = np.cumprod(facs) * iPropSpending.investedAmount
        fig3, ax3 = plt.subplots()
        ax3.bar(np.arange(1, nyrs + 1), lbVals, color='r', linewidth=2)
        ax3.set(xlabel='Year', ylabel='Lockbox Equivalent Initial Value',
                title='Lockbox Equivalent Initial Values')
        ax3.grid()
        plt.show()

    # Create vector of initial portfolio values
    portvals = np.ones((nscen, 1)) * iPropSpending.investedAmount

    # Initialize desired spending matrix
    desiredSpendingM = np.zeros((nscen, nyrs))
    # Initialize incomes and fees matrices
    incsM = np.zeros((nscen, nyrs))
    feesM = np.zeros((nscen, nyrs))

    
    # Compute incomes paid at the beginning of year 1
    year1Income = portvals * spendProps[0] # MS - got a broadcast error trying to do it in one line so I broke it up
    incsM[:,0] = year1Income[:,0]

    # Compute portfolio values after income payments
    portvals = portvals - incsM[:, 0].reshape(-1, 1) 


    # Compute incomes and fees paid at the beginning of each subsequent year
    for yr in range(1, nyrs):
        # Compute portfolio values before deductions
        portvals = portvals * retsM[:, yr - 1].reshape(-1,1) 
        # Compute and deduct fees paid at the beginning of the year
        feesV = (1 - rr) * portvals
        feesM[:, yr] = feesM[:, yr] + feesV.reshape(-1) 
        portvals = portvals - feesV
        # Compute incomes paid out at the beginning of the year in states 1, 2, or 3
        v = (client.pStatesM[:, yr] > 0) & (client.pStatesM[:, yr] < 4)
        yearStartIncomes = v.reshape(-1,1) * (portvals * spendProps[yr])
        incsM[:, yr] = yearStartIncomes.flatten() 
                            
        # Pay the entire value if in state 4
        v = (client.pStatesM[:, yr] == 4)
        incsM[:, yr] = incsM[:, yr] + (v.reshape(-1,1) * portvals).flatten()
        # Deduct incomes paid from portfolio values
        portvals = portvals - incsM[:, yr].reshape(-1,1)

    # Add incomes and fees to client matrices
    client.incomesM = client.incomesM + incsM
    client.feesM = client.feesM + feesM

    return client
