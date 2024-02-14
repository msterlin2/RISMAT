import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

def anal_plot_yoy_incomes(analysis, client, market, plottype, states):
    # initialize graph
    #plt.figure(figsize=(max(0, analysis.figPosition[0]), max(0, analysis.figPosition[1])))
    # Create chart
    fig, ax = plt.subplots()
    fig.canvas.manager.set_window_title(f'YOYIncomes {plottype}')
    plt.title(f'YOYIncomes {plottype}')
    plt.xlabel(f'Year t {plottype}Income')
    plt.ylabel(f'Year t+1 {plottype}Income')
    plt.grid(True)
    

    # make plottype lower case
    plottype = plottype.lower()

    # set real or nominal text
    if 'n' in plottype:
        rntext = 'Nominal '
    else:
        rntext = 'Real '

    # set states text
    statestext = f'States: {states}'

    # convert client incomes to nominal values if required
    if 'n' in plottype:
        client.incomesM = market.cumCsM * client.incomesM

    # set labels
    plt.xlabel(f'Year t {rntext}Income')
    plt.ylabel(f'Year t+1 {rntext}Income')
    #plt.title(f'Year over Year {rntext}Incomes: {statestext}, Year t:', fontsize=12)
    ttl = (f'Year over Year {rntext}Incomes: {statestext}, Year t:')

    # create matrix with 1 for each personal state to be included
    cells = np.zeros_like(client.pStatesM)
    for state in states:
        cells += (client.pStatesM == state)

    # find last year with income for personal states
    nyrs = np.max(np.where(np.sum(cells, axis=0) > 0))

    # modify matrices
    incs = client.incomesM[:, :nyrs]
    cells = cells[:, :nyrs]
    
    # set axes
    ii = np.where(cells > 0)
    maxval = np.max(incs[ii])
    minval = np.min(incs[ii])
    if analysis.plotYOYIncomesWithZero == 'y':
        minval = 0
    plt.axis([minval, maxval, minval, maxval])

    # initialize plot
    plt.grid(True)
    #plt.plot([minval, maxval], [minval, maxval], linewidth=1, color='k')  # 45-degree line

    # set colors for states 0,1,2,3, and 4
    # orange; red; blue; green; orange;
    cmap = np.array([[1, 0.5, 0], [1, 0, 0], [0, 0, 1], [0, 0.8, 0], [1, 0.5, 0]])
    # set full color based on states
    clrmat = np.array([cmap[state] for state in states])
    clr_full = np.mean(clrmat, axis=0)
    # set shade color
    shade = analysis.animationShadowShade
    clr_shade = shade * clr_full + (1 - shade) * np.array([1, 1, 1])

    # set delay change parameter
    delays = analysis.animationDelays
    delay_change = (delays[1] - delays[0]) / (nyrs - 1)
    # set initial delay
    delay = delays[0]

    # plot incomes
    for col in range(1, nyrs):
        
        ttl1 = f'{ttl} {col - 1} ' 
        plt.title(ttl1, color='b')

        col1 = col - 1
        col2 = col

        cellmat = cells[:, col1:col2 +1] #MS Need to get both col1 and col2, col1:col2 gets upto but not including col2 so adding +1

        ii = np.where(np.sum(cellmat, axis=1) >= 2)

        x = incs[ii,col1]
        y = incs[ii,col2]
        x= x.reshape(-1) #MS - This speeds up the graph 
        y= y.reshape(-1)
        plt.plot(x, y, '.', color=clr_full, linewidth=2)
        plt.plot([minval, maxval], [minval, maxval], linewidth=2, color='k') # plot 45 degree line

        plt.pause(delay)
        delay += delay_change

        plt.plot(x, y, '.', color=clr_shade, linewidth=2)
        
    plt.show()