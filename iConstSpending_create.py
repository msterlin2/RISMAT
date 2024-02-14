import numpy as np

class IConstSpending:
    
    def __init__(self) -> None:
        # create a constant spending income data structure
    
        # amount invested
        self.investedAmount = 100000

        # proportion of initial investment spent in the first year
        self.initialProportionSpent = 0.040

        # relative incomes for personal states 1, 2, and 3
        # (any remaining value is paid in personal state 4)
        self.pStateRelativeIncomes = [0.5, 0.5, 1.0]

        # graduation ratio of each real income relative to the prior income distribution
        self.graduationRatio = 1.00

        # matrix of points on market proportion glide path graph
        # top row is y: market proportions (between 0.0 and 1.0 inclusive)
        # bottom row is x: years (first must be 1 or greater)
        # the first proportion applies to years up to and at the first year
        # the last proportion applies to years at and after the last year
        # proportions between two years are interpolated linearly
        self.glidePath = np.array([[1.0], [1]])

        # show glide path (y or n)
        self.showGlidePath = 'n'

        # retention ratio for investment returns for the portfolio
        # = 1 - expense ratio
        # e.g. expense ratio = 0.10% per year, retentionRatio = 0.999
        self.retentionRatio = 0.999

def iConstSpending_create():
    return IConstSpending()