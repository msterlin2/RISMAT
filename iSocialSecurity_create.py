class iSocialSecurity:
    def __init__(self):
        # Incomes in state 1, last column repeated for subsequent years
        self.state1Incomes = [float('inf'), 30000]

        # Incomes in state 2, last column repeated for subsequent years
        self.state2Incomes = [float('inf'), 30000]

        # Incomes for state 3, last column repeated for subsequent years
        self.state3Incomes = [44000]

def iSocialSecurity_create():
    return iSocialSecurity()