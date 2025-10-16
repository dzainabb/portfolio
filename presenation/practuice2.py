#MULTIPLE COUNTRIES DIVORCE VS WORK

import pandas as pd
import matplotlib.pyplot as plt

# Read CSVs
x_data = pd.read_csv('/Users/sabiqadar/Downloads/annual-working-hours-per-worker/annual-working-hours-per-worker.csv')
y_data = pd.read_csv('/Users/sabiqadar/Downloads/divorces-per-1000-people/divorces-per-1000-people.csv')

# Parameters
countries = ['United Kingdom', 'United States', 'Mexico']
start_year = 2013
end_year = 2019

# Merge datasets on Entity and Year
merged = pd.merge(
    x_data[['Entity','Year','Working hours per worker']],
    y_data[['Entity','Year','Crude divorce rate']],
    on=['Entity','Year']
)

# Filter by countries and years
filtered = merged[(merged['Entity'].isin(countries)) & 
                  (merged['Year'] >= start_year) & 
                  (merged['Year'] <= end_year)]

# Plot each country
plt.figure(figsize=(8,5))
for country in countries:
    country_data = filtered[filtered['Entity'] == country]
    plt.plot(country_data['Working hours per worker'], 
             country_data['Crude divorce rate'],
             marker='o', linestyle='-', label=country)

plt.xlabel('Average Hours Worked - annually')
plt.ylabel('Crude Divorce Rate')
plt.title(f'Line Graph from {start_year} to {end_year}')
plt.legend()
plt.grid(True)
plt.show()
