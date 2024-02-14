class iLBAnnuity:
    def __init__(self):
        # create a Lockbox Annuity data structure
        # uses only TIPS and market holdings

        # relative payments from lockboxes (2* client number of years)
        # row 1: tips
        # row 2: market portfolio
        self.proportions = []

        # first income year
        self.firstIncomeYear = 1

        # relative incomes for personal states 1,2,3 and 4
        self.pStateRelativeIncomes = [0.5, 0.5, 1.0, 0]

        # graduation ratio of each real income distribution relative to the prior distribution
        self.graduationRatio = 1.00

        # retention ratio for investment returns for tips and market portfolio
        # = 1 - expense ratio
        # e.g. expense ratio = 0.10% per year, retentionRatio = 0.999
        self.retentionRatios = [0.999, 0.999]

        # ratio of value invested in lockboxes to initial cost
        self.valueOverCost = 0.90

        # cost
        self.cost = 100000


def iLBAnnuity_create():
    # create a Lockbox Annuity data structure
    return iLBAnnuity()