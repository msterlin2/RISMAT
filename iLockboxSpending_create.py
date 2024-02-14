class iLockboxSpending:
    def __init__(self):
        # create a lockbox spending data structure

        # Amount invested
        self.investedAmount = 100000

        # Relative payments from lockboxes: size(2, client number of years)
        # Row 1: tips, 
        # Row 2: market portfolio
        # May be provided by AMDnLockboxes.proportions, CMULockboxes.proportions,
        # CombinedLockboxes.proportions, or otherwise
        # Note: lockboxes are to be spent for personal states 1, 2, 3, or 4
        self.lockboxProportions = []

        # Bequest utility ratio
        # Ratio of utility per dollar for bequest versus spending
        # Note: this applies equally for personal states 1, 2, and 3
        self.bequestUtilityRatio = 0.50

        # Show lockbox amounts (y or n)
        self.showLockboxAmounts = 'y'


def iLockboxSpending_create():
    return iLockboxSpending()
