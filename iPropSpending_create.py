class iPropSpending:
    def __init__(self):
        # create a proportional spending income data structure
        
        # Amount invested
        self.investedAmount = 100000

        # Use IRS Required Minimum Distributions (RMD) Life Expectancies (y or n)
        self.useRMDlifeExpectancies = 'y'

        # If RMD not used, vector of life expectancies and age for the first value
        self.nonRMDlifeExpectancies = []
        self.nonRMDfirstLEAge = 70

        # Current age of the portfolio owner
        self.portfolioOwnerCurrentAge = 65

        # Show proportions spent (y or n)
        self.showProportionsSpent = 'n'

        # Show Lockbox equivalent initial investment values
        self.showLockboxEquivalentValues = 'n'

        # Matrix of points on the portfolio market proportion glide path graph
        # Top row is y: market proportions (between 0.0 and 1.0 inclusive)
        # Bottom row is x: years (first must be 1 or greater)
        # The first proportion applies to years up to and at the first year
        # The last proportion applies to years at and after the last year
        # Proportions between two years are interpolated linearly
        self.glidePath = [[1.0], [1]]

        # Show portfolio glide path (y or n)
        self.showGlidePath = 'n'

        # Retention ratio for portfolio investment returns
        # = 1 - expense ratio
        # e.g. expense ratio = 0.10% per year, retentionRatio = 0.999
        self.retentionRatio = 0.999

def iPropSpending_create():
    return iPropSpending()