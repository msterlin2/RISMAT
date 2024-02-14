import matplotlib.pyplot as plt
import numpy as np
from analPlotSurvivalProbabilities import anal_plot_survival_probabilities
from analPlotScenarios import analPlotScenarios
from analPlotIncomeDistributions import analPlotIncomeDistributions
from analPlotIncomeMaps import anal_plot_income_maps
from analPlotYOYIncomes import anal_plot_yoy_incomes
from analPlotRecipientPVs import anal_plot_recipient_pvs
from analPlotPPCSandIncomes import anal_plot_ppcs_and_incomes
from analPlotYearlyPVs import anal_plot_yearly_pvs
from analPlotEfficientIncomes import analPlotEfficientIncomes

def analysis_process(analysis, client, market):
    
    analysis = initialize(analysis, client)
    
    # analysis: plot survival probabilities
    if analysis.plotSurvivalProbabilities == 'y':
        anal_plot_survival_probabilities(analysis, client, market)
    
    # analysis: plot scenarios
    if analysis.plotScenarios == 'y':
        types = analysis.plotScenariosTypes
        for t in types:
            analPlotScenarios(analysis, client, market, t)
    
    # analysis: plot income distributions
    if analysis.plotIncomeDistributions == 'y':
        # find states
        states = analysis.plotIncomeDistributionsStates
        # find types
        types = analysis.plotIncomeDistributionsTypes
        # create figures
        for i in range(len(types)):
            for j in range(len(states)):
                # create Figure
                fig, ax = plt.subplots()
                fig.canvas.manager.set_window_title('Income Distributions')
        
                # call external function analPlotIncomeDistributions
                analPlotIncomeDistributions(analysis, client, market, types[i], states[j])
                
    # analysis: plot income maps
    if analysis.plotIncomeMaps == 'y':
        # find states
        states = analysis.plotIncomeMapsStates
        # find types
        types = analysis.plotIncomeMapsTypes
        # create figures
        for i in range(len(types)):
            for j in range(len(states)):
                # create Figure
                fig, ax = plt.subplots()
                fig.canvas.manager.set_window_title('Income Maps')
                
                # call external function analPlotIncomeMaps
                anal_plot_income_maps(analysis, client, market, types[i], states[j])

    # analysis: plot year over year incomes
    if analysis.plotYOYIncomes == 'y':
        # find states
        states = analysis.plotYOYIncomesStates
        # find types
        types = analysis.plotYOYIncomesTypes
        # create figures
        for i in range(len(types)):
            for j in range(len(states)):
                # create Figure
                # call external function analPlotYOYIncomes
                anal_plot_yoy_incomes(analysis, client, market, types[i], states[j])                

    # analysis: plot recipient present values
    if analysis.plotRecipientPVs == 'y':
        # call external function analPlotRecipientPVs
        anal_plot_recipient_pvs(analysis, client, market)

    # analysis: plot PPCs and Incomes
    if analysis.plotPPCSandIncomes == 'y':
        # find states
        states = analysis.plotPPCSandIncomesStates
        # create figures
        for i in range(len(states)):
            # create Figure
            #fig, ax = plt.subplots()
            #fig.canvas.manager.set_window_title(f'PPCs and Incomes - State {states[i]}')
            
            # call external function analPlotPPCSandIncomes
            anal_plot_ppcs_and_incomes(analysis, client, market, states[i])

    # analysis: plot yearly PVs
    if analysis.plotYearlyPVs == 'y':
        # find states
        states = analysis.plotYearlyPVsStates
        # create figures
        for i in range(len(states)):
            # create Figure
            fig, ax = plt.subplots()
            fig.canvas.manager.set_window_title(f'Yearly PVs - State {states[i]}')
            
            # call external function analPlotYearlyPVs
            anal_plot_yearly_pvs(analysis, client, market, states[i])

    # analysis: plot efficient incomes
    if analysis.plotEfficientIncomes == 'y':
        # find states
        states = analysis.plotEfficientIncomesStates
        # find types
        types = analysis.plotEfficientIncomesTypes
        # create figures
        for i in range(len(types)):
            for j in range(len(states)):
                # create Figure
                fig, ax = plt.subplots()
                fig.canvas.manager.set_window_title(f'Efficient Incomes - Type {types[i]}, State {states[j]}')
                
                # call external function analPlotEfficientIncomes
                analPlotEfficientIncomes(analysis, client, market, types[i], states[j])

    
    finish(analysis)
    return analysis


def initialize(analysis, client):
    #MS Commenting the initial figure below as this just seems to create an extra blank figure
    #MS Leaving it in for consistency with the matlab code
    '''
    figsize = client.figureSize
    if len(figsize) < 2:
        ss = plt.gcf().get_size_inches() #* np.array([1, 1])
        figsize[0] = 0.9 * ss[0]
        figsize[1] = 0.9 * ss[1]

    figw, figh = figsize
    ss = plt.gcf().get_size_inches() #* np.array([1, 1])
    x1 = (ss[0] - figw) / 2
    x2 = (ss[1] - figh) / 2
    analysis.figPosition = [x1, x2, figw, figh]
    '''
    analysis.figNum = 1
    analysis.stack = []
    
    return analysis


def createFigure(analysis):
    #MS - This function is not used, but remains here for consistency with the matlab code

    fignum = plt.figure().number
    plt.gcf().set_size_inches(analysis.figPosition[2], analysis.figPosition[3])
    analysis.stack.append(fignum)
    plt.set_cmap('viridis')
    
    ax = plt.gca()
    
    for item in ([ax.title, ax.xaxis.label, ax.yaxis.label] +
                 ax.get_xticklabels() + ax.get_yticklabels()):
        item.set_fontsize(12)

    plt.gcf().set_facecolor([1, 1, 1])
    
    if analysis.stackFigures.lower() == 'n':
        if len(analysis.stack) > 2:
            plt.close(analysis.stack[0])
            analysis.stack = analysis.stack[1:]
    
    return analysis


def processFigure(analysis):
    #MS - This function is not used, but remains here for consistency with the matlab code
    
    analysis.figNum += 1

    if analysis.figureDelay > 0:
        plt.pause(analysis.figureDelay)
    else:
        plt.pause(0.001)
    
    return analysis


def finish(analysis):
    
    if analysis.stackFigures.lower() == 'n':
        if len(analysis.stack) > 1:
            plt.close(analysis.stack[0])

    if analysis.figuresCloseWhenDone == 'y':
        plt.close('all')
    