class IFixedAnnuity:
    def __init__(self) -> None:
        # guaranteed relative or absolute incomes for years 1,...
        self.guaranteedIncomes = []
        # relative incomes in the first post-guarantee year for personal states 0,1,2,3, and 4
        self.pStateIncomes = [0, 0.5, 0.5, 1, 0]
        # graduation ratio of each post-guarantee income to prior post-guarantee income
        self.graduationRatio = 1.00
        # type of incomes (real 'r' or nominal 'n');
        self.realOrNominal = 'r'
        # ratio of value to initial cost
        self.valueOverCost = 0.90
        # cost
        self.cost = 100000

def iFixedAnnuity_create():
    return IFixedAnnuity()
