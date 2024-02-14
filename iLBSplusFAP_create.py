class iLBSplusFAP():
    def __init__(self):
        # creates a data structure for a combination of lockbox spending
        #   and future purchase of an annuity
        
        # Lockbox proportions (matrix with TIPS in the top row, market in the bottom row)
        self.lockboxProportions = []

        # Lockbox spending bequest utility ratio for spending
        self.bequestUtilityRatio = 0.50

        # Year in which the annuity is to be purchased
        self.annuitizationYear = 20

        # Set initial proportion in TIPS for the lockbox to be used to purchase the annuity
        self.FAPlockboxProportionInTIPS = 0.50

        # Annuity ratio of value to initial cost
        self.annuityValueOverCost = 0.90

        # Percentile of the income distribution to match for FAP and the last spending lockbox (0 to 100)
        self.incomePercentileToMatch = 75

        # Total amount invested
        self.amountInvested = 100000


def iLBSplusFAP_create():
    return iLBSplusFAP()
