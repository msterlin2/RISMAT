import numpy as np
from client_create import client_create
from client_process import client_process
from market_create import market_create
from market_process import market_process
from iFixedAnnuity_create import iFixedAnnuity_create
from iFixedAnnuity_process import iFixedAnnuity_process
from analysis_create import analysis_create
from analysis_process import analysis_process

# Create a new client data structure
client = client_create()

# Change client data elements as needed
# ...

# Process the client data structure
client = client_process(client)

# Create a new market data structure
market = market_create()

# Change market data elements as needed
# ...

# Process the market data structure
market = market_process(market, client)

# Create a fixed annuity
iFixedAnnuity = iFixedAnnuity_create()

# Change fixed annuity data elements as needed
# ...

# Process fixed annuity and update client matrices
client = iFixedAnnuity_process(iFixedAnnuity, client, market)

# create analysis
analysis = analysis_create()

# select desired output
analysis.plotSurvivalProbabilities = 'y';

# process analysis
analysis_process(analysis, client, market);
