import numpy as np
import matplotlib.pyplot as plt

def analPlotScenarios(analysis, client, market, plottype):
    # Create chart
    fig, ax = plt.subplots()
    fig.canvas.manager.set_window_title(f"Scenarios: {plottype}")
    
    # Make plottype lower case
    plottype = plottype.lower()

    # Add labels
    plt.title(f"Scenarios: {plottype}")
    plt.xlabel('Year')
    if 'r' in plottype:
        plt.ylabel('Real Income, Estate, or Fees')
    else:
        plt.ylabel('Nominal Income, Estate, or Fees')

    plt.grid(True)
    plt.gca().set_facecolor((1, 1, 1))  # Set background color

    # Set colors for states 0, 1, 2, 3, 4, and fees (5)
    cmap = [[1, 0.5, 0], [1, 0, 0], [0, 0, 1], [0, 0.8, 0], [1, 0.5, 0], [0, 0, 0]]

    # Convert client income and fees to nominal values if required
    if 'n' in plottype:
        client.incomesM = market.cumCsM * client.incomesM
        client.feesM = market.cumCsM * client.feesM

    # Extract sample matrices for at least 100 scenarios
    n = max(100, analysis.plotScenariosNumber)
    nscen, nyrs = client.incomesM.shape
    firstScen = np.random.randint(1, nscen - n + 1)
    lastScen = firstScen + n - 1
    scenPStates = client.pStatesM[firstScen:lastScen, :]
    scenIncomes = client.incomesM[firstScen:lastScen, :]
    scenFees = client.feesM[firstScen:lastScen, :]

    # Set personal states to be shown
    states = [1, 2, 3] if 'i' in plottype else []
    if 'e' in plottype:
        states.append(4)

    # Find maximum value for y-axis
    incomeCells = np.zeros_like(scenPStates)
    for i in states:
        incomeCells += (scenPStates == i)

    maxIncome = 1.01 * np.max(np.max((incomeCells > 0) * scenIncomes))

    # If fee is to be included, find maximum fee for sample states
    maxFee = np.max(np.max(scenFees)) if 'f' in plottype else 0

    # Set maximum for y-axis
    maxY = 1.01 * max(maxIncome, maxFee)

    # Set axes
    plt.axis([0, nyrs, 0, maxY])

    # Set shade and delay parameter
    shade = analysis.animationShadowShade
    delays = analysis.animationDelays
    delayChange = (delays[1] - delays[0]) / (analysis.plotScenariosNumber - 1)

    # Show scenarios
    delay = delays[0]
    for scenNum in range(1, analysis.plotScenariosNumber + 1):
        # Plot incomes
        incomes = scenIncomes[scenNum - 1, :]
        pstates = scenPStates[scenNum - 1, :]
        for pstate in states:
            x = np.where(pstates == pstate)[0]
            if len(x) > 0:
                y = incomes[x]
                plt.plot(x, y, '-*', color=cmap[pstate], linewidth=2.5)

        # Plot fees
        if 'f' in plottype:
            fees = scenFees[scenNum - 1, :]
            plt.plot(range(1, nyrs + 1), fees, '*', color=cmap[5], linewidth=2.5)

        # Pause
        plt.pause(delay)
        delay += delayChange

        # Re-plot incomes using shading
        for pstate in states:
            x = np.where(pstates == pstate)[0]
            if len(x) > 0:
                y = incomes[x]
                clr = shade * np.array(cmap[pstate]) + (1 - shade) * np.array([1, 1, 1])

                plt.plot(x, y, '-*', color=clr, linewidth=2.5)

        # Re-plot fees using shading
        if 'f' in plottype:
            clr = shade * np.array(cmap[5]) + (1 - shade) * np.array([1, 1, 1])
            plt.plot(range(1, nyrs + 1), fees, '*', color=clr, linewidth=2.5)

    plt.show()

    return client