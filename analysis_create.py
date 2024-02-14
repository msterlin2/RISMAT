class Analysis:
    def __init__(self) -> None:
        # Function to create an analysis data structure
        self.caseName = 'Smith Case'
        # animation first and last delay times in seconds
        self.animationDelays = [0.01, 0.005]
        # animation shadow shade of original (0 to 1)
        self.animationShadowShade =  0.2
        # delay time between figures (0 for beep and keypress) in seconds
        self.figureDelay =  0
        # stack figures or replace each one with the next
        self.stackFigures =  'n'
        # close figures when done
        self.figuresCloseWhenDone =  'n'

        # plot survival probabilities -- y/n
        self.plotSurvivalProbabilities =  'n'

        # plot scenarios
        self.plotScenarios =  'n'
        # plot scenarios: set of cases with real (r) or nominal (n) and 
        #   income (i), estate (e) and/or fees (f)
        self.plotScenariosTypes =  ['ri', 'rie', 'rif', 'rief']
        # plot scenarios: number of scenarios
        self.plotScenariosNumber =  10

        # plot income distributions 
        self.plotIncomeDistributions =  'n'
        # plot income distributions: set of cases with real or nominal (r/n) and 
        #   conditional or unconditional (c/u) types
        self.plotIncomeDistributionsTypes =  ['rc', 'ru', 'nc', 'nu']
        # plot income distributions: sets of states (one set per graph)
        self.plotIncomeDistributionsStates =  [[3], [1, 2]]
        # plot income distributions: minimum percent of scenarios
        self.plotIncomeDistributionsMinPctScenarios =  0.5
        # proportion of incomes to be shown
        self.plotIncomeDistributionsProportionShown =  1.00
        #  plot income distributions: percent of maximum income plotted
        self.plotIncomeDistributionsPctMaxIncome =  100

        # plot income maps 
        self.plotIncomeMaps =  'n'
        # plot income maps: set of value types -- real or nominal (r/n) and
        #   conditional or unconditional (c/u) types
        self.plotIncomeMapsTypes =  ['ru', 'rc']
        # plot income maps: sets of states (one set per graph)
        self.plotIncomeMapsStates =  [[3], [1, 2]]
        # plot income maps: minimum percent of scenarios
        self.plotIncomeMapsMinPctScenarios =  0.5
        # plot income maps: percent of maximum income plotted
        self.plotIncomeMapsPctMaxIncome =  100

        # plot year over year incomes
        self.plotYOYIncomes =  'n'
        # plot year over year incomes -- real or nominal (r/n) 
        self.plotYOYIncomesTypes =  ['r' 'n']
        # plot year over year incomes -- sets of states (one set per graph)
        self.plotYOYIncomesStates =  [[3], [1, 2]]
        # plot year over year incomes -- include zero (y/n)
        self.plotYOYIncomesWithZero =  'n' # y

        # plot recipient present values -- y (yes) or n (no)
        self.plotRecipientPVs =  'n'

        # plot PPCs and Incomes -- y/n
        self.plotPPCSandIncomes =  'n'
        # plot PPC and Incomes -- semilog or loglog
        self.plotPPCSandIncomesSemilog =  'n' # y
        # plot PPCs and Incomes -- sets of states (one set per graph)
        self.plotPPCSandIncomesStates =  [[3]]
        # plot PPCs and Incomes: minimum percent of scenarios
        self.plotPPCSandIncomesMinPctScenarios =  0.5

        # plot yearly present values -- y (yes) or n (no)
        self.plotYearlyPVs =  'n'
        # plot yearly present values-- sets of states (one set per graph)
        self.plotYearlyPVsStates =  [[3], [1], [2]]
        # plot yearly present values: minimum percent of scenarios
        self.plotYearlyPVsMinPctScenarios =  0.5

        # plot efficient incomes -- y (yes) or n (no)
        self.plotEfficientIncomes =  'n'
        # plot efficient incomes -- sets of states (one set per graph)
        self.plotEfficientIncomesStates =  [[3], [1, 2]]
        # plot points (actual) curves (efficient) and/or 
        #   lines (two-asset market-based strategies
        #   combinations of (p,c,l) -- one graph per type
        self.plotEfficientIncomesTypes =  ['pcl']
        # plot efficient incomes: minimum percent of scenarios
        self.plotEfficientIncomesMinPctScenarios =  0.5

def analysis_create():    
    return Analysis()