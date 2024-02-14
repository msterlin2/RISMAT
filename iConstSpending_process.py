import matplotlib.pyplot as plt
import numpy as np

def iConstSpending_process(iConstSpending, client, market):
    # get matrix dimensions
    nscen, nyrs = market.rmsM.shape

    # get glide path
    path = iConstSpending.glidePath
    path = np.array(path)

    # get points from glide path
    ys = path[0, :] 
    xs = path[1, :]

    ys = np.array(ys) 
    xs = np.array(xs)
    
    # insure no years prior to 1
    xs = np.maximum(xs, 1)

    # insure no market proportions greater than 1 or less than 0
    ys = np.minimum(ys, 1)
    ys = np.maximum(ys, 0)

    # sort points in increasing order of x values
    ii = np.argsort(xs)
    xs = xs[ii] 
    ys = ys[ii]

    # Add values for year 1 and/or last year if needed
    if xs[0] > 1:
        xs = np.insert(xs, 0, 1)
        ys = np.insert(ys, 0, ys[0])
    if xs[-1] < nyrs:
        xs = np.append(xs, nyrs)
        ys = np.append(ys, ys[-1])
        
    # create vectors for all years
    pathxs = []
    pathys = []
    for i in range(len(xs) - 1):
        xlft = xs[i]
        xrt = xs[i + 1]
        ylft = ys[i]
        yrt = ys[i + 1]

        pathxs.extend([xlft])
        pathys.extend([ylft])
        

        if xlft != xrt:
            slope = (yrt - ylft) / (xrt - xlft)
            for x in range(int(xlft) + 1, int(xrt)):
                pathxs.extend([x])
                
                yy = ylft + slope * (x - xlft)
                pathys.extend([yy])
                

    pathxs.extend([xs[-1]])
    pathys.extend([ys[-1]])
    

    # show glide path if desired
    if iConstSpending.showGlidePath.lower() == 'y':
        fig, ax = plt.subplots()
        #MS - skipping formatting commands
        #plt.figure(figsize=(12, 8))
        #plt.figure()
        #plt.rcParams.update({'font.size': 10})
        #plt.xlabel('Year ', fontsize=10)
        #plt.ylabel('Proportion in Market Portfolio   ', fontsize=10)
        ax.plot(path[1, :], path[0, :], '*b', linewidth=4)
        ax.plot(xs, ys, '-r', linewidth=2)
        ax.legend(['Input', 'All'])
        ax.set_xlabel('Year')
        ax.set_ylabel('Proportion in Market Portfolio')
        fig.canvas.manager.set_window_title('Glide Path: Market Proportions by Year  ')
        ax.grid()
        plt.show()

    # create matrix of gross returns for the investment strategy
    retsM = np.zeros((nscen, nyrs))
    for yr in range(nyrs - 1):
        rets = pathys[yr] * market.rmsM[:, yr]
        rets = rets + (1 - pathys[yr]) * market.rfsM[:, yr]
        retsM[:, yr] = rets

    # get retention ratio
    rr = iConstSpending.retentionRatio

    # create vector of initial portfolio values
    portvals = np.ones(nscen) * iConstSpending.investedAmount

    # initialize desired spending matrix
    desiredSpendingM = np.zeros((nscen, nyrs))

    # create matrix of desired real spending for the highest personal state
    prop = iConstSpending.initialProportionSpent
    amt = prop * iConstSpending.investedAmount
    gradRatio = iConstSpending.graduationRatio
    factors = np.power(gradRatio, np.arange(nyrs))

    # create matrix of maximum desired spending
    maxSpendingM = np.ones((nscen, 1)) * (amt * factors)

    # add amounts to desired spending matrix
    props = iConstSpending.pStateRelativeIncomes
    props = props / np.max(props)
    props = np.maximum(props, 0)
    for ps in range(1, 4):
        s = maxSpendingM * props[ps - 1]
        m = (client.pStatesM == ps) * s
        desiredSpendingM = desiredSpendingM + m

    # initialize incomes and fees matrices
    incsM = np.zeros((nscen, nyrs))
    feesM = np.zeros((nscen, nyrs))

    # compute incomes paid at the beginning of year 1
    incsM[:, 0] = np.minimum(desiredSpendingM[:, 0], portvals)
    # compute portfolio values after income payments
    portvals = portvals - incsM[:, 0]

    # compute incomes and fees paid at the beginning of each subsequent year
    for yr in range(1, nyrs):
        # compute portfolio values before deductions
        portvals = portvals * retsM[:, yr - 1]
        # compute and deduct fees paid at the beginning of the year
        feesV = (1 - rr) * portvals
        feesM[:, yr] = feesV
        portvals = portvals - feesV
        # compute incomes paid out at the beginning of the year in states 1, 2, or 3
        v = (client.pStatesM[:, yr] > 0) & (client.pStatesM[:, yr] < 4)
        incsM[:, yr] = v * np.minimum(desiredSpendingM[:, yr], portvals)
        # pay the entire value if state 4
        v = (client.pStatesM[:, yr] == 4)
        incsM[:, yr] = incsM[:, yr] + v * portvals
        # deduct incomes paid from portfolio values
        portvals = portvals - incsM[:, yr]

    # add incomes and fees to client matrices
    client.incomesM = client.incomesM + incsM
    client.feesM = client.feesM + feesM

    return client