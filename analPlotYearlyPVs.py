import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

def anal_plot_yearly_pvs(analysis, client, market, states):
    # add labels
    plt.title('Yearly PVs', color='b')
    plt.xlabel('Year')
    plt.ylabel('Present Value')
    plt.grid(True)
    plt.legend(['Efficient PV', 'Inefficient PV'])

    '''  #MS - Ran into errors with the colors so this is commented out and python will handle the colors.
         # But keeping it here for consistency with the matlab code 
    '''
    # set colors for states 0,1,2,3,and 4
    # orange; red; blue; green; orange; black
    cmap = np.array([[1, 0.5, 0], [1, 0, 0], [0, 0, 1], [0, 0.8, 0], [1, 0.5, 0]])
    # set efficient PV color based on states
    clrmat = np.array([cmap[state] for state in states])
    clr_pv = np.mean(clrmat, axis=0)
    # set inefficiency color
    clr_ineff = np.array([0, 0, 0])
    
    clr_pv = np.array(clr_pv)
    clr_ineff = np.array(clr_ineff)

    #colormap = mcolors(np.append(clr_pv, clr_ineff))
    custom_cmap = mcolors.LinearSegmentedColormap.from_list("custom_cmap", [clr_pv, clr_ineff])

    #plt.register_cmap(name='custom_colormap', cmap=colormap)
    #plt.imshow(colormap, aspect='auto')
    #plt.set_cmap(np.concatenate((clr_pv, clr_ineff), axis=0))   
    #plt.set_cmap(np.concatenate((clr_pv[np.newaxis, :], clr_ineff[np.newaxis, :]), axis=0))
    #plt.colorbar(plt.cm.ScalarMappable(cmap=custom_cmap))
    
    # get matrix size
    nscen, nyrs = client.pStatesM.shape

    # set delay change parameter 
    delays = analysis.animationDelays
    delay_change = (delays[1] - delays[0]) / (nyrs - 1)

    # set initial delay
    delay = delays[0]

    # create matrix with 1 for each personal state to be included
    cells = np.zeros(client.pStatesM.shape)
    
    for state in states:
        cells = cells + (client.pStatesM == state)

    # find last year with sufficient included states
    nscen, nyrs = cells.shape
    numstates = np.sum(cells > 0, axis=0)
    min_prop = analysis.plotYearlyPVsMinPctScenarios
    min_num = int(min_prop / 100 * nscen)
    last_year = max(np.where(numstates > min_num)[0] + 1)
    last_year = np.max(np.where(numstates > min_num, np.arange(1, nyrs + 1), 0))
    if last_year == 0:
        print('Insufficient scenarios')
        return

    # truncate matrices
    cellsM = cells[:, :last_year]
    incsM = client.incomesM[:, :last_year]
    ppcsM = market.ppcsM[:, :last_year]

    # set up valuation vectors
    total_pvs = []
    eff_pvs = []

    # get present values
    for yr in range(last_year):
        rows = np.where(cells[:, yr] > 0)[0]
        pvs = market.pvsM[rows, yr]
        incs = client.incomesM[rows, yr]
        total_pv = np.dot(pvs.T, incs)
        eff_pv = np.dot(np.sort(pvs), np.sort(incs)[::-1])
        total_pvs.append(total_pv)
        eff_pvs.append(eff_pv)

    # compute total efficiency
    total_eff = 100 * (sum(eff_pvs) / sum(total_pvs))

    # title
    ttl1 = f'Yearly Present Values, States = {states}  '
    ttl2 = f'Overall Efficiency = {round(total_eff, 1)}%  '
    plt.title(ttl1 + '\n' + ttl2, color='b')

    # scale axes
    plt.axis([0, last_year + 1, 0, max(total_pvs)])

    # plot pvs
    diffs = np.array(total_pvs) - np.array(eff_pvs)
    #plt.bar(range(1, last_year + 1), [eff_pvs, diffs], stacked=True)
    plt.bar(range(1, last_year + 1), eff_pvs, label='Efficient PVs')
    plt.bar(range(1, last_year + 1), diffs, bottom=eff_pvs, label='Differences')

    plt.legend()
    plt.show()