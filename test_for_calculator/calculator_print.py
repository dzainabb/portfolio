import numpy as np

# get the current date
date_today = np.datetime64('today', 'D')

print("Today's date:")
print(date_today)


date = input('Enter a date: (YYYY-MM-DD)')


date1 = np.datetime64(date_today)
date2 = np.datetime64(date)

num_of_days = date1 - date2

print(num_of_days)