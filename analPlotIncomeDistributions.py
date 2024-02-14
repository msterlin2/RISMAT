import numpy as np
import matplotlib.pyplot as plt

def analPlotIncomeDistributions(analysis, client, market, plottype, states):
    # Initialize graph
    
    plt.title(f'Income Distributions {plottype}')
    plt.xlabel('Income (x)')
    plt.ylabel(f'Probability Income Exceeds x')
    plt.grid(True)

    # Make plottype lower case
    plottype = plottype.lower()

    # Set colors for states 0, 1, 2, 3, and 4
    cmap = np.array([[1, 0.5, 0], [1, 0, 0], [0, 0, 1], [0, 0.8, 0], [1, 0.5, 0]])

    # Set condition labels
    condition = 'if ' if 'c' in plottype else 'and '

    # Set real or nominal text
    rntext = 'Nominal ' if 'n' in plottype else 'Real '

    # Set states text
    statestext = f"{condition}States = {states}"

    # Set labels
    plt.xlabel(f'{rntext}Income (x)')
    plt.ylabel(f'Probability {rntext}Income Exceeds x')
    ttlstart = f'{rntext}Incomes {statestext}: Year '

    # Create matrix with 1 for each personal state to be included
    cells = np.zeros_like(client.pStatesM)
    for s in states:
        cells += (client.pStatesM == s)

    # Convert client incomes to nominal values if required
    if 'n' in plottype:
        client.incomesM = market.cumCsM * client.incomesM

    # Create vector with the number of scenarios for each year
    nScen = np.sum(cells, axis=0)

    # Find the number of years to plot
    nyrs = np.sum(nScen > 0)

    # Find the maximum income
    incomes = client.incomesM * cells
    maxIncome = np.max(np.max(incomes))

    # Set axes for the figure
    prop = 0.01 * analysis.plotIncomeDistributionsPctMaxIncome
    maxIncome = prop * maxIncome
    propShown = analysis.plotIncomeDistributionsProportionShown

    if propShown < 1.0:
        ii = np.where(cells == 1)[0]
        #v = np.sort(incomes[ii])
        v = np.sort(incomes[ii], axis=None)  # Ensure incomes are flattened for sorting
        i = int(propShown * len(v))
        i = max(1, i)
        #maxIncome = np.max(np.max(v))
        maxIncome = v[i-1]

    ax = [0, maxIncome, 0, 1]
    plt.axis(ax)

    # Set delay change parameter
    delays = analysis.animationDelays
    delayChange = (delays[1] - delays[0]) / (nyrs - 1)

    # Set initial delay
    delay = delays[0]

    # Set parameters
    clrmat = np.array([cmap[s] for s in states])
    clrFull = np.mean(clrmat, axis=0)

    # Set shade color
    shade = analysis.animationShadowShade
    clrShade = shade * clrFull + (1 - shade) * np.array([1, 1, 1])

    # Set initial delay
    delay = delays[0]

    # Plot each year's distribution
    for yr in range(1, nyrs + 1):
        # Find values for y-axis
        rows = np.where(cells[:, yr - 1] == 1)[0]
        incomes = client.incomesM[rows, yr - 1]
        yx = np.arange(1, len(incomes) + 1)
        yx = yx / len(yx) if 'c' in plottype else yx / client.nScenarios

        # Compute probability of states and round to one decimal place
        probPstates = len(incomes) / client.nScenarios
        probPstates = round(1000 * probPstates) / 10

        # Plot if probability large enough
        if probPstates >= analysis.plotIncomeDistributionsMinPctScenarios:
            plt.plot(np.sort(incomes), np.sort(yx)[::-1], color=clrFull, linewidth=3)
            ttl1 = f'{ttlstart}{yr}'
            ttl2 = f'{probPstates} Percent of Scenarios'
            plt.title(ttl1 + '\n' + ttl2, color='b')
            plt.pause(delay)
            plt.plot(np.sort(incomes), np.sort(yx)[::-1], color=clrShade, linewidth=3)
            delay = delay + delayChange

    plt.show()