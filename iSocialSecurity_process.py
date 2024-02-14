import numpy as np

def iSocialSecurity_process(iSocialSecurity, client, market):
    """
    Creates social security income matrix and then adds values to client incomes matrix.
    """

    # Get number of scenarios and years
    nscen, nyrs = client.pStatesM.shape

    # Save personal states
    pStatesM = client.pStatesM

    # Create social security incomes matrix
    incomesM = np.zeros((nscen, nyrs))

    # Add incomes for personal state 3
    #extend input vector
    vec = np.array([iSocialSecurity.state3Incomes])
    
    if len(vec) > nyrs:
        vec = vec[:nyrs]
    lastval = vec[-1]
    vec = np.append(vec, lastval * np.ones(nyrs - len(vec)))

    # Create matrix with incomes for personal state 3
    allIncomes = np.ones((nscen, 1)) * vec
    states = (pStatesM == 3)
    stateIncomes = states * allIncomes
    incomesM += stateIncomes

    # Add incomes for personal states 1 and 2
    for s in [1, 2]:
        # Get input matrix
        m = np.array([iSocialSecurity.state1Incomes]) if s == 1 else np.array([iSocialSecurity.state2Incomes])
    
        # Extend input matrix
        nrows, ncols = m.shape
        if ncols > nyrs:
            m = m[:, :nyrs]
            ncols = nyrs
        lastcol = m[:, ncols - 1]
        numadd = nyrs - ncols
        if numadd > 0:
            m = np.hstack((m, np.tile(lastcol[:, None], (1, numadd))))

        # Process all but last row
        for i in range(nrows):
            # get row from matrix
            incrow = m[i, :]
    
            # find column for last 3
            last3col = np.sum(incrow == np.Inf)
            # replace inf with zero in incrow
            incrow[:last3col] = 0
            # create vector with s in pStateM rows with desired sequence of 3 and s
            psrows = (pStatesM[:, last3col] == 3) & (pStatesM[:, last3col] == s)
            # make matrix with incrow in every eligible row
            mm = psrows[:, None] * incrow
            # set all cells with state not equal to s to zero
            mm = mm * (pStatesM == s)
            # add incomes to matrix
            incomesM += mm
            

        # Process last row
        # get row from matrix
        incrow = m[nrows - 1, :]
        # find column for last 3
        last3col = np.sum(incrow == np.Inf)
        # replace Inf with zero in incrow
        incrow[:last3col] = 0
        # create vector with 1 in pStateM rows with >= the number of 3s
        psrows = (pStatesM[:, last3col] == 3)
        # make matrix with incrow in every eligible row
        mm = psrows[:, None] * incrow
        # set all cells with state not equal to s to zero
        mm = mm * (pStatesM == s)
        # add to incomes matrix
        incomesM += mm
        
    # Add incomes to client incomes
    client.incomesM += incomesM

    return client
