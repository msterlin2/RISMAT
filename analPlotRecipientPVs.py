import numpy as np
import matplotlib.pyplot as plt

def anal_plot_recipient_pvs(analysis, client, market):
    # compute values for state incomes
    pvs = []
    for state in range(5):  # MATLAB 0:4 is equivalent to Python range(5)
        ii = np.where(client.pStatesM == state)
        # Transpose market.pvsM[ii] and multiply with client.incomesM[ii]
        pv = np.dot(market.pvsM[ii].T, client.incomesM[ii])
        pvs.append(pv)
    
    # add states 0 to state 4 for estate total
    pvs = [pvs[i] for i in range(1, 4)] + [pvs[0] + pvs[4]]
    
    # Compute fees
    fees = np.sum(market.pvsM * client.feesM)
        
    # Add fees to present values
    pvs.append(fees)
    
    # compute total value and create string in $thousands
    total_val = np.sum(pvs)
    total_val_str = f"{round(float(total_val) / 1000)}"

    # if any value is zero change to small positive value
    pvs = [pv if pv != 0 else 0.00001 for pv in pvs]

    # compute proportions
    props = 100 * (pvs / np.sum(pvs))

    # Create chart
    fig, ax = plt.subplots()
    fig.canvas.manager.set_window_title('Recipient Present Values')
    
    # Create legends
    legends = [
        f"{client.p1Name}: {props[0]:.1f} %",
        f"{client.p2Name}: {props[1]:.1f} %",
        f"Both: {props[2]:.1f} %",
        f"Estate: {props[3]:.1f} %",
        f"Fees: {props[4]:.1f} %"
    ]

    # Create chart
    if np.min(props) >= 0:
        # Create a pie chart
        #if np.min(props) > 0.05:
        #    labels = [client.p1Name, client.p2Name, 'Both', 'Estate', 'Fees']
        #else:
        #    labels = ['', '', '', '', '']
        labels = [client.p1Name if props[0] > 0.05 else '',
                  client.p2Name if props[1] > 0.05 else '',
                  'Both' if props[2] > 0.05 else '',
                  'Estate' if props[3] > 0.05 else '',
                  'Fees' if props[4] > 0.05 else '']

        patches, texts, autotexts = ax.pie(props, labels=labels, colors=['red', 'blue', 'green', 'orange', 'black'], autopct='%1.1f%%', startangle=90)
        
        plt.legend(legends, loc='lower right', bbox_to_anchor=(1.3, -0.1))
    else:
        # Create a bar chart
        ax.bar(range(len(props)), props, color=['red', 'blue', 'green', 'orange', 'black'])
        plt.grid(True)
        plt.ylabel('Percent of Total Value')
        ax.set_xticklabels([client.p1Name, client.p2Name, 'Both', 'Estate', 'Fees'])
    
    # Add title
    plt.title(f"Recipient Present Values\nTotal Value = ${total_val_str} thousand", color='blue')
    
    plt.show()