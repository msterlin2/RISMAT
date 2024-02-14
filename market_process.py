import numpy as np

def market_process(market, client):
    # Get size for all matrices from client.pStatesM
    nrows, ncols = client.pStatesM.shape

    # Compute cost of living (inflation) matrix
    u = market.eC
    v = market.sdC**2
    b = np.sqrt(np.log((v/(u**2)) + 1))
    a = 0.5 * np.log((u**2)/np.exp(b**2))
    market.csM = np.exp(a + b*np.random.randn(nrows, ncols))

    # Compute cumulative cost of living (inflation) matrix
    m = np.cumprod(market.csM, axis=1) 
    market.cumCsM = np.hstack((np.ones((nrows, 1)), m[:, :ncols-1]))

    # Compute risk-free real returns matrix
    market.rfsM = market.rf * np.ones((nrows, ncols))

    # Compute cumulative risk-free real returns matrix at ends of each year
    m = np.cumprod(market.rfsM, axis=1)
    market.cumRfsM = np.hstack((np.ones((nrows, 1)), m[:, :ncols-1]))
    
    # Compute market returns matrix
    u = market.exRm + (market.rf - 1)
    v = market.sdRm**2
    b = np.sqrt(np.log((v/(u**2)) + 1))
    a = 0.5 * np.log((u**2)/np.exp(b**2))
    market.rmsM = np.exp(a + b*np.random.randn(nrows, ncols))

    # Compute market cumulative returns matrix
    m = np.cumprod(market.rmsM, axis=1) 
    #market.cumRmsM = np.column_stack([np.ones(nrows), m[:, :ncols-1]])
    market.cumRmsM = np.hstack((np.ones((nrows, 1)), m[:, 0:ncols-1]))
    
    # Compute ppcs and present values matrix
    b = np.log(u / market.rf) / np.log(1 + (market.sdRm ** 2) / (u ** 2))
    a = np.sqrt(u * market.rf) ** (b - 1)
    as_matrix = np.ones((nrows, 1)) * (a**np.arange(ncols))
    market.ppcsM = as_matrix * (market.cumRmsM**-b)
    market.pvsM = market.ppcsM / nrows

    # Temporary
    market.avec = as_matrix[0, :]
    market.b = b
    
    return market