import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Load data
data = pd.read_csv('/Users/sabiqadar/Downloads/divorces-per-1000-people/divorces-per-1000-people.csv')

# Optional: filter for one country (e.g., Australia)
united_kingdom = data[data['Entity'] == 'United Kingdom']

slope, intercept, r_value, p_value, std_err = stats.linregress(
    united_kingdom['Year'], united_kingdom['Crude divorce rate']
)

line = slope * united_kingdom['Year'] + intercept


# Create scatter plot
plt.scatter(united_kingdom['Year'], united_kingdom['Crude divorce rate'], color='teal', alpha=0.8, label = 'Data')

plt.plot(united_kingdom['Year'], line, color='blue', label='Regression Line')

equation_text = f"y = {slope:.3f}x + {intercept:.2f}\nR² = {r_value**2:.3f}"
plt.text(united_kingdom['Year'].min(), united_kingdom['Crude divorce rate'].max(),
         equation_text, fontsize=10, color='blue', ha='left', va='center')


# Add labels and title
plt.xlabel('Year')
plt.ylabel('Crude Divorce Rate (per 1000 people)')
plt.title('Divorce Rate Over Time - United Kingdom')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.show()

