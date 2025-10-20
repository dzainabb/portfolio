#calculator for random dates in csv file - calculating dates difference

import numpy as np
import pandas as pd

random_dates = pd.read_csv('/Users/sabiqadar/Downloads/random_dates.csv')
print(random_dates.head(3))


date_today = np.datetime64('today', 'D')    
print("Today's date:")
print(date_today)
