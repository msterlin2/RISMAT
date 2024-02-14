import matplotlib.pyplot as plt
import numpy as np

def combinedLockboxes_process(combinedLockboxes, market, client):
    # combines componentLockboxes in combinedLockboxes to create a new lockbox
    n = len(combinedLockboxes.componentLockboxes)
    wts = combinedLockboxes.componentWeights
    wts = np.maximum(wts, 0)  # Ensure weights are non-negative
    wts /= np.sum(wts)  # Normalize weights
    
    # Initializes combined properties
    boxprops = combinedLockboxes.componentLockboxes[0].proportions
    combprops = wts[0] * boxprops
    
    # Combine properties of each lockbox
    for i in range(1, n):
        boxprops = combinedLockboxes.componentLockboxes[i].proportions
        combprops += wts[i] * boxprops

    combinedLockboxes.proportions = combprops

    xs = combinedLockboxes.proportions
    nyrs = xs.shape[1]
    
    # plot contents if requested
    if combinedLockboxes.showCombinedProportions.lower() == 'y':
        #xs = combinedLockboxes.proportions
        #nyrs = xs.shape[1]
        
        fig, ax = plt.subplots()
        # Generate a sequence of numbers
        # x = np.arange(1, nyrs + 1)
        x = np.arange(1, xs.shape[1] + 1)

        # Stacked bar plot
        for i in range(xs.shape[0]):
            ax.bar(x, xs[i, :], bottom=np.sum(xs[:i, :], axis=0))
        
        # Grid, font size, and figure position settings
        ax.grid(True)

        # MS - skipping formatting below
        #ss = client.figurePosition
        #fig.set_size_inches(ss[2]/fig.dpi, ss[3]/fig.dpi)
        # fig.set_facecolor((1, 1, 1))
        
        ax.set_xlabel('Lockbox Maturity Year')
        ax.set_ylabel('Amount Invested at Inception')
        ax.legend(['TIPS', 'Market'])
        ax.set_title(f"Lockbox Proportions for {combinedLockboxes.title}", color='b')
        #plt.xticks()
        #plt.yticks()

        # Axis limits
        ax.set_xlim(0, nyrs + 1)
        ax.set_ylim(0, 1)
        
        plt.show()

        return combinedLockboxes