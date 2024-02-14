import matplotlib.pyplot as plt
import numpy as np

def CMULockboxes_process(CMULockboxes, market, client):
    # computes lockbox proportions for a CMULockbox strategy
    
    # get number of years
    nscen, nyrs = market.cumRmsM.shape
    
    # set proportions for year 1
    mktprop = CMULockboxes.initialMarketProportion
    mktprop = min(1, max(0, mktprop))  # Ensure mktprop is between 0 and 1
    tipsprop = 1 - mktprop
    
    # find ratio of market proportion each year to that for the prior year
    a = market.avec[1]
    b = market.b
    logk = (-np.log(1 / a)) / b
    k = np.exp(logk)
    
    # compute market proportions for all years
    mktprops = mktprop * np.power(1 / k, np.arange(nyrs))

    # compute TIPS proportions for all years
    tipsprops = tipsprop * np.power(1 / market.rf, np.arange(nyrs))

    # compute lockbox proportions
    CMULockboxes.proportions = np.array([tipsprops, mktprops])

    # plot contents if requested
    if CMULockboxes.showProportions.lower() == 'y':
        xs = CMULockboxes.proportions
        fig, ax = plt.subplots()
        x = np.arange(1, xs.shape[1] + 1)

        # Stacked bar plot
        ax.bar(x, xs[0, :], label='TIPS')
        ax.bar(x, xs[1, :], bottom=xs[0, :], label='Market')
        
        ax.grid(True)
        #MS skipping some chart formatting commands from the matlab code
        
        ax.set_xlabel('Lockbox Maturity Year')
        ax.set_ylabel('Amount Invested at Inception')
        ax.legend(['TIPS', 'Market'])
        ax.set_title('Lockbox Proportions for Constant Marginal Utility', color='b')
        
        # Axis limits
        ax.set_xlim(0, nyrs + 1)
        ax.set_ylim(0, 1)
        
        plt.show()

        return CMULockboxes