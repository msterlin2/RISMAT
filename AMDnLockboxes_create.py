class AMDnLockboxes:
    def __init__(self)-> None:
        # Creates an AMDn lockboxes data structure
        
        # year of cumulative market return distribution to approximate (n)
        # note: n must be greater or equal to 2
        self.cumRmDistributionYear = 2

        # lockbox proportions (computed by AMDnLockboxes_process)
        self.proportions = []

        # show lockbox contents (y or n)
        self.showProportions = 'n'

def AMDnLockboxes_create():
    return AMDnLockboxes()
