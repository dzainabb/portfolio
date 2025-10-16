import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read your combined CSV file
df = pd.read_csv('/Users/sabiqadar/Library/Application Support/Microsoft/working_divorce.csv')

# Parameters
countries = ['United Kingdom', 'United States']  # two countries to compare
start_year = 2000
end_year = 2019

# Filter data
filtered = df[(df['Entity'].isin(countries)) &
              (df['Year'] >= start_year) &
              (df['Year'] <= end_year)]

# Pivot so we have years as rows and countries as columns
pivot_hours = filtered.pivot(index='Year', columns='Entity', values='Working hours per worker')
pivot_divorce = filtered.pivot(index='Year', columns='Entity', values='Crude divorce rate')

# --- Plot 1: Working Hours ---
plt.figure(figsize=(10, 6))
x = np.arange(len(pivot_hours.index))
width = 0.35

plt.bar(x - width/2, pivot_hours[countries[0]], width, label=countries[0])
plt.bar(x + width/2, pivot_hours[countries[1]], width, label=countries[1])

plt.xticks(x, pivot_hours.index, rotation=45)
plt.xlabel('Year')
plt.ylabel('Working Hours per Worker')
plt.title(f'Average Annual Working Hours: {countries[0]} vs {countries[1]} ({start_year}–{end_year})')
plt.legend()
plt.tight_layout()
plt.show()

# --- Plot 2: Divorce Rate ---
plt.figure(figsize=(10, 6))
plt.bar(x - width/2, pivot_divorce[countries[0]], width, label=countries[0])
plt.bar(x + width/2, pivot_divorce[countries[1]], width, label=countries[1])

plt.xticks(x, pivot_divorce.index, rotation=45)
plt.xlabel('Year')
plt.ylabel('Crude Divorce Rate (per 1,000 people)')
plt.title(f'Crude Divorce Rate: {countries[0]} vs {countries[1]} ({start_year}–{end_year})')
plt.legend()
plt.tight_layout()
plt.show()
