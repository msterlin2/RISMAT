class CMULockboxes:
    def __init__(self) -> None:
        # creates a CMU lockboxes data structure

        # initial lockbox market proportion: 0 to 1.0 inclusive
        self.initialMarketProportion = 1.0
    
        # lockbox proportions (computed by CMULockboxes_process)
        self.proportions = []
        
        # show lockbox contents (y or n)
        self.showProportions = 'n'
        
def CMULockboxes_create():
    return CMULockboxes()