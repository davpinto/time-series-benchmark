import pandas as pd
from pandas_datareader import get_data_yahoo
from datetime import datetime
from plotnine import *

itub = get_data_yahoo("itub", "1990-01-01")
itub.reset_index(drop=False, inplace=True)
itub['Date'] = pd.to_datetime(itub['Date'])

ggplot(itub, aes(x='Date', y='Open')) + \
    geom_line()