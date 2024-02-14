import numpy as np
import matplotlib.pyplot as plt

def analPlotEfficientIncomes(analysis, client, market, types, states):
    # Add labels
    plt.title('Efficient Real Incomes')
    plt.xlabel('Cumulative Market Real Return')
    plt.ylabel('Real Income')
    plt.grid(True)

    # Set colors for points for states 0,1,2,3,and 4 
    # orange; red; blue; green; orange; black
    cmap = np.array([[1, 0.5, 0], [1, 0, 0], [0, 0, 1], [0, 0.8, 0], [1, 0.5, 0]])
    clrmat = cmap[states]
    clrPoints = np.mean(clrmat, axis=0)

    # Set point shadow shade color
    shade = analysis.animationShadowShade
    clrPointsShade = shade * clrPoints + (1 - shade) * np.array([1, 1, 1])

    # Set curve color and shade color
    clrCurve = [0, 0, 0]
    clrCurveShade = shade * np.array(clrCurve) + (1 - shade) * np.array([1, 1, 1])

    # Set line color and shade color
    clrLine = [1, 0.5, 0]
    clrLineShade = shade * np.array(clrLine) + (1 - shade) * np.array([1, 1, 1])

    # Create matrix with 1 for each personal state to be included
    cells = np.zeros_like(client.pStatesM)
    for s in states:
        cells += (client.pStatesM == s)

    # Find last year with sufficient included states
    numstates = np.sum(cells > 0, axis=0)
    minprop = analysis.plotEfficientIncomesMinPctScenarios
    minnum = (minprop / 100) * client.nScenarios
    lastyear = max(np.where(numstates > minnum)[0])
    if lastyear == 0:
        plt.title('Insufficient scenarios')
        plt.show()
        return

    # Set initial delay and change parameter
    delays = analysis.animationDelays
    delay = delays[0]
    delayChange = (delays[1] - delays[0]) / (lastyear - 1)
    
    # Truncate matrices
    cellsM = cells[:, :lastyear]
    incsM = client.incomesM[:, :lastyear]
    cumretsM = market.cumRmsM[:, :lastyear]
    pvsM = market.pvsM[:, :lastyear]

    # Find maximum incomes
    maxincs = np.max(np.max(incsM * cellsM))

    # Find maximum cumulative market return for x-axis
    # Includes 99.9% of possible values
    cumretm = cumretsM * cellsM
    cumretv = np.sort(cumretm[cumretm > 0])
    maxcumrets = cumretv[int(0.999 * len(cumretv))]

    # Scale axes
    plt.axis([0, maxcumrets, 0, maxincs])

    # Plot results
    for yr in range(1, lastyear + 1):
        # Get data for year
        rows = np.where(cells[:, yr - 1] > 0)[0]
        pvs = pvsM[rows, yr - 1]
        incs = incsM[rows, yr - 1]
        cumrets = cumretsM[rows, yr - 1]

        # Sort data
        cumretsS = np.sort(cumrets)
        incsS = np.sort(incs)
        pvsS = np.sort(pvs)[::-1]

        # Plot points if desired
        if 'p' in types:
            plt.plot(cumrets, incs, '*', color=clrPoints)

        # Fit line for regression of sorted incomes and cumrets
        # incomeS = b(1) + b(2) * cumretS
        xvals = np.vstack([np.ones(len(cumretsS)), cumretsS]).T
        b = np.linalg.lstsq(xvals, incsS, rcond=None)[0]

        # Compute fitted incomes using regression equation
        incsFitted = b[0] + b[1] * cumretsS
        # Compute present value of the original set of incomes
        pvIncs = np.sum(pvs * incs)
        # Compute present value of the fitted line
        pvLine = np.sum(pvsS * incsFitted)
        pvLine = np.sum(pvsS * np.sort(incsFitted))
        # Find additional income for each scenario
        delta = (pvIncs - pvLine) / np.sum(pvs)
        # Increase each fitted income by a constant so pv = original amount
        incsFitted = incsFitted + delta

        # Plot sorted cumrets and incomes if desired
        if 'c' in types:
            plt.plot(cumretsS, incsS, '*', color=clrCurve)

        # Plot fitted line if desired
        if 'l' in types and yr > 1:
            plt.plot([0] + cumretsS.tolist(), [b[0] + delta] + incsFitted.tolist(), color=clrLine, linewidth=4)

        # Add title
        ttl1 = f'Efficient Real Incomes Year, {yr} States: {states}'
        plt.title(ttl1, color='b')

        # Pause
        plt.pause(delay)

        # Shade points if plotted
        if 'p' in types:
            plt.plot(cumrets, incs, '*', color=clrPointsShade)

        # Shade sorted cumrets and incomes if plotted
        if 'c' in types:
            plt.plot(cumretsS, incsS, '*', color=clrCurveShade)

        # Shade fitted line if plotted
        if 'l' in types and yr > 1:
            plt.plot([0] + cumretsS.tolist(), [b[0] + delta] + incsFitted.tolist(), color=clrLineShade, linewidth=4)

        # Pause
        plt.pause(delay)

        # Change delay time
        delay -= delayChange
        
    plt.show()