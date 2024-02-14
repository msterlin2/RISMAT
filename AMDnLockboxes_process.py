import numpy as np
import matplotlib.pyplot as plt

def AMDnLockboxes_process(AMDnLockboxes, market, client):
    # get number of years of returns
    nscen, nyrs = market.cumRmsM.shape
    
    # get n
    n = AMDnLockboxes.cumRmDistributionYear
    n = max(min(n,nyrs),2)
    
    # set lockbox proportions for initial years to investment in the market portfolio
    xfs = np.zeros(n-1)
    xms = np.ones(n-1)
    
    # create matrix of proportions
    xs = np.array([xfs, xms])

    # do regressions to compute contents of remaining lockboxes
    for yr in range(n, nyrs + 1):  
        # sort cumulative returns
        x = np.sort(market.cumRmsM[:, yr - 1 ]) 
        y = np.sort(market.cumRmsM[:, n - 1])

        # regress y values on x values
        # y = b(1) + b(2)*x
        xvals = np.vstack([np.ones(len(x)), x]).T
        b = np.linalg.lstsq(xvals, y, rcond=None)[0]

        # compute lockbox contents
        xf = b[0] / np.mean(market.cumRfsM[:, yr - 1]) 
        xm = b[1]

        # add to xs matrix
        xs = np.hstack((xs, [[xf], [xm]]))
        
    # add lockbox holdings to AMDnLockboxes
    AMDnLockboxes.proportions = xs

    # plot contents if requested
    if AMDnLockboxes.showProportions.lower() == 'y':
        fig, ax = plt.subplots()
        x = np.arange(1, xs.shape[1] + 1)
        ax.bar(x, xs[0].T)
        ax.bar(x, xs[1].T, bottom=xs[0].T)
        plt.grid(True)
        fig.patch.set_facecolor('white')
        plt.xlabel('Lockbox Maturity Year ', fontsize=10)
        plt.ylabel('Amount Invested at Inception   ', fontsize=10)
        plt.legend(['TIPS', 'Market'])
        plt.axis([0, nyrs + 1, 0, 1])
        t = f'Lockbox Contents for Approximating Market Distribution in year {n}'
        plt.title(t, fontsize=10, color='b')
        plt.show()
        plt.pause(1)  # Pause for a brief moment to display the plot

    return AMDnLockboxes