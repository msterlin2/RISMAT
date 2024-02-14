class CombinedLockboxes:
    def __init__(self) -> None:
        # creates a lockbox by combining other lockboxes

        # lockboxes to be combined (data structures)
        self.componentLockboxes = []

        # proportions of lockboxes being combined
        #    one value for each lockbox; values greater than or equal to 0
        #    values will be normalized to sum to 1.0
        self.componentWeights = []

        # title of combined lockboxes
        self.title = 'Combined Lockboxes'

        # combined lockboxes proportions produced by combinedLockboxes_process
        self.proportions = []

        # show combined lockbox contents (y or n)
        self.showCombinedProportions = 'n'

def combinedLockboxes_create():
    return CombinedLockboxes()