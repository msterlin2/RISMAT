class IFAPLockbox:
    def __init__(self) -> None:
        # year in which annuity is to be purchased
        self.yearOfAnnuityPurchase = 20

        # initial proportion ($) in TIPS in lockbox (0 to 1.0)
        # with the remainder in the market portfolio
        self.proportionInTIPS = 0.50

        # initial amount ($) in the lockbox
        self.investedAmount = 100000

        # annuity ratio of value to initial cost
        self.annuityValueOverCost = 0.90


def iFAPlockbox_create():
    return IFAPLockbox()