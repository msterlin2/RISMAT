import numpy as np
import matplotlib.pyplot as plt

def anal_plot_ppcs_and_incomes(analysis, client, market, states):
    # initialize graph
    #plt.figure(figsize=(max(0, analysis.figPosition[0]), max(0, analysis.figPosition[1])))
    fig, ax = plt.subplots()
    t = 'PPCs and Real Incomes '
    plt.title(t, fontsize=10, color='b')

    plt.grid(True)

    # set labels
    plt.ylabel('log ( Price per Chance )  ')
    plt.xlabel('Real Income  ')

    # set colors for states 0, 1, 2, 3, and 4
    cmap = np.array([[1, 0.5, 0], [1, 0, 0], [0, 0, 1], [0, 0.8, 0], [1, 0.5, 0]])

    # set full color based on states
    clrmat = np.array([cmap[s] for s in states])
    clr_full = np.mean(clrmat, axis=0)

    # set shade color
    shade = analysis.animationShadowShade
    clr_shade = shade * clr_full + (1 - shade) * np.array([1, 1, 1])

    # get matrix size
    nscen, nyrs = client.pStatesM.shape

    # set delay change parameter
    delays = analysis.animationDelays
    delay_change = (delays[1] - delays[0]) / (nyrs - 1)

    # create matrix with 1 for each personal state to be included
    cells = np.zeros(client.pStatesM.shape, dtype=int)
    for s in states:
        cells += (client.pStatesM == s)

    # find last year with sufficient included states
    numstates = np.sum(cells > 0, axis=0)
    minprop = analysis.plotPPCSandIncomesMinPctScenarios
    minnum = (minprop / 100) * nscen
    lastyear = max(np.where(numstates > minnum)[0] + 1)  # +1 due to 0-indexing
    
    if lastyear == 0:
        plt.title('Insufficient scenarios')
        plt.show()
        return

    # truncate matrices
    cellsM = cells[:, :lastyear]
    incsM = client.incomesM[:, :lastyear]
    ppcsM = market.ppcsM[:, :lastyear]

    
    # find maximum and minimum incomes
    ii = np.where(cellsM > 0)
    incsvec = incsM[ii]
    maxinc, mininc = np.max(incsvec), np.min(incsvec)

    # find maximum and minimum PPCs
    ppcsvec = ppcsM[ii]
    maxppc, minppc = np.max(ppcsvec), np.min(ppcsvec)

    # set initial delay
    delay = delays[0]

    # if minimum income is zero, require semilog
    if mininc == 0:
        analysis.plotPPCSandIncomesSemilog = 'y'

    if analysis.plotPPCSandIncomesSemilog == 'y':
        # set axes and label
        plt.axis([0, maxinc, np.log(minppc), np.log(maxppc)])

        for yr in range(lastyear):
            # get data
            cellsv = cellsM[:, yr]
            ii = np.where(cellsv > 0)[0]
           
            incs = incsM[ii, yr]
            ppcs = ppcsM[ii, yr]

            # title
            ttl1 = f'PPCs and Real Incomes, States =  {states}  '
            ttl2 = f'Year: {yr}  '
            plt.title(ttl1 + '\n' + ttl2, color='b')
            
            # plot points
            plt.plot(incs, np.log(ppcs), '*', color=clr_full, linewidth=0.5)
            plt.pause(delay)

            # shade points
            delay += delay_change
            plt.plot(incs, np.log(ppcs), '*', color=clr_shade, linewidth=0.5)

    else:
        # set axes and labels
        plt.xlabel('log ( Real Income )  ')
        plt.axis([np.log(mininc), np.log(maxinc), np.log(minppc), np.log(maxppc)])

        for yr in range(lastyear):
            # get data
            cellsv = cellsM[:, yr]
            ii = np.where(cellsv > 0)[0]
        
            incs = incsM[ii, yr]
            ppcs = ppcsM[ii, yr]

            # title
            ttl1 = f'PPCs and Real Incomes, States =  {states}  '
            ttl2 = f'Year: {yr}  '
            plt.title(ttl1 + '\n' + ttl2, color='b')
            
            # plot points
            plt.plot(np.log(incs), np.log(ppcs), '*', color=clr_full, linewidth=0.5)
            plt.pause(delay)

            # shade points
            delay += delay_change
            plt.plot(np.log(incs), np.log(ppcs), '*', color=clr_shade, linewidth=0.5)

    plt.show()
