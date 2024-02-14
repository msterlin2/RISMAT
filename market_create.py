class Market:
    def __init__(self) -> None:
        # Create a market data structure with default values
        # Cost of living
        self.eC = 1.02   # Expected cost of living ratio
        self.sdC = 0.01  # Standard deviation of cost of living ratios
        
        # Risk-free real investments
        self.rf = 1.01  # Risk-free real return rate

        # Market portfolio returns
        self.exRm = 1.0425  # Market portfolio expected return over risk-free rate
        self.sdRm = 0.125   # Market portfolio standard deviation of return

def market_create():
    return Market()
