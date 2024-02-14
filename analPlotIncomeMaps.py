import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors

def anal_plot_income_maps(analysis, client, market, plottype, states):
    # initialize graph
    plt.grid(True)

    # make plottype lower case
    plottype = plottype.lower()

    # set real or nominal text
    if 'n' in plottype:
        rntext2 = 'Nominal '
    else:
        rntext2 = 'Real '
    if 'c' in plottype:
        rntext1 = 'Conditional'
    else:
        rntext1 = ''

    # set states text
    statestext = f'States = {states}'

    # convert client incomes to nominal values if required
    if 'n' in plottype:
        client.incomesM = market.cumCsM * client.incomesM

    # create matrix with 1 for each personal state to be included
    nscenarios = client.pStatesM.shape[0]
    cells = np.zeros_like(client.pStatesM)
    for s in states:
        cells += (client.pStatesM == s)

    # make matrix with incomes for included personal states
    incomes = cells * client.incomesM

    # find cells with included personal states
    ii = np.where(cells > 0)

    # find minimum and maximum incomes for included personal states
    mininc = np.min(incomes[ii])
    maxinc = np.max(incomes[ii])

    # find last year with sufficient included states
    numstates = np.sum(cells > 0, axis=0)
    minprop = analysis.plotIncomeMapsMinPctScenarios
    minnum = (minprop / 100) * nscenarios
    lastyear = np.max((numstates > minnum) * np.arange(1, numstates.size + 1))
    
    # reduce matrices to cover only included years
    incomes = incomes[:, :lastyear]
    cells = cells[:, :lastyear]

    # Create colormap
    map = plt.cm.get_cmap('jet')
    colors = map(np.arange(map.N))

    # Modify the first color to white
    colors[0] = (1, 1, 1, 1)  # RGBA for white color

    # Create a new colormap from the modified color array
    custom_map = matplotlib.colors.ListedColormap(colors)

    # Apply the colormap
    plt.colormap = custom_map

    # put a lower value in each excluded personal state
    ii = np.where(cells < 1)
    incomes[ii] = mininc - 1

    # make changes if map is to be conditional
    if 'c' in plottype:
        # convert to conditional incomes
        cond_incomes = []
        for yr in range(incomes.shape[1]):
            # extract values for chosen personal states
            yr_incomes = incomes[:, yr]
            yr_cells = cells[:, yr]
            ii = np.where(yr_cells > 0)[0]
            vals = yr_incomes[ii]
            # create full vector of values greater than the minimum
            num = len(vals)
            m = np.tile(vals, int(np.ceil(nscenarios / num)))
            # extract the first nscen values as a vector
            v = m[:nscenarios]
            cond_incomes.append(v)

        incomes = np.column_stack(cond_incomes)

    # truncate incomes above percentage of maximum income
    prop = 0.01 * analysis.plotIncomeMapsPctMaxIncome
    maxinc = prop * np.max(np.max(incomes[:, :lastyear]))
    incomes[:, :lastyear] = np.minimum(maxinc, incomes[:, :lastyear])

    # plot
    plt.imshow(np.sort(incomes[:, :lastyear], axis=0), aspect='auto', extent=[0, lastyear, 0, 1], cmap=custom_map)
    colorbar = plt.colorbar()
    colorbar.ax.tick_params()  # Set the font size for ticks on the colorbar
    plt.xticks()
    plt.yticks()

    # set labels
    plt.xlabel('Year')
    plt.ylabel(f'Probability of Exceeding {rntext2}Income')
    title_text = f'{rntext1} Probabilities of Exceeding {rntext2}Income in {statestext}'
    plt.title(title_text, color='b')

    plt.show()