import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

def anal_plot_survival_probabilities(analysis, client, market):
    """
    Plot recipient survival probabilities.

    Parameters:
    - analysis (dict): Analysis parameters.
    - client (Client): Client data structure.
    - market (Market): Market data structure.
    - figsize (tuple): Figure size (default is (10, 10)).
    """
    # Constants
    COMBINED_STATE = 3

    # Get probabilities of survival
    prob_survive_1_only = np.mean(client.pStatesM == 1, axis=0)
    prob_survive_2_only = np.mean(client.pStatesM == 2, axis=0)
    prob_survive_both = np.mean(client.pStatesM == COMBINED_STATE, axis=0)
    prob_survive_all = np.vstack((prob_survive_both, prob_survive_1_only, prob_survive_2_only))

    # Create graph
    fig, ax = plt.subplots()
    fig.canvas.manager.set_window_title('Recipient Survival Probabilities')

    ax.bar(np.arange(len(prob_survive_all[0])), prob_survive_all[0], color='green', label='Both')
    ax.bar(np.arange(len(prob_survive_all[1])), prob_survive_all[1], bottom=prob_survive_all[0], color='red', label=client.p1Name + ' only')
    ax.bar(np.arange(len(prob_survive_all[2])), prob_survive_all[2], bottom=prob_survive_all[0] + prob_survive_all[1], color='blue',
           label=client.p2Name + ' only')

    ax.grid(True)
    ax.set_title('Recipient Survival Probabilities', color=(0, 0, 1))
    ax.set_xlabel('Year')
    ax.set_ylabel('Probability')
    ax.legend()

    # color mapping
    cmap = [(0, 0.8, 0), (1, 0, 0), (0, 0, 1)]
    custom_cmap = mcolors.LinearSegmentedColormap.from_list("custom_cmap", cmap)
  
    plt.show()
