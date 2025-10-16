#DIFF COUNTRIES AND DIVORCE AND WORK
import pandas as pd
import matplotlib.pyplot as plt

# === 1. Load datasets ===
divorce_df = pd.read_csv('/Users/sabiqadar/Downloads/divorces-per-1000-people/divorces-per-1000-people.csv')
hours_df = pd.read_csv('/Users/sabiqadar/Downloads/annual-working-hours-per-worker/annual-working-hours-per-worker.csv')

# === 2. Merge datasets on Entity, Code, and Year ===
merged_df = pd.merge(
    hours_df, divorce_df,
    on=['Entity', 'Code', 'Year'],
    suffixes=('_hours', '_divorce')
)

# === 3. Choose countries to plot ===
countries = ['United Kingdom', 'United States']  # You can change this list

# === 4. Create figure ===
fig, ax1 = plt.subplots(figsize=(12,6))

# Colors for each country (extend list if needed)
colors = ['tab:blue', 'tab:red']

# === 5. Plot working hours (Left Y-axis) ===
for i, country in enumerate(countries):
    data = merged_df[merged_df['Entity'] == country]
    ax1.plot(
        data['Year'], data['Working hours per worker'],
        color=colors[i],
        linestyle='-',
        label=f'{country} - Working Hours'
    )

ax1.set_xlabel('Year')
ax1.set_ylabel('Working Hours per Worker')
ax1.tick_params(axis='y', labelcolor='black')

# === 6. Plot divorce rate (Right Y-axis) ===
ax2 = ax1.twinx()

for i, country in enumerate(countries):
    data = merged_df[merged_df['Entity'] == country]
    ax2.plot(
        data['Year'], data['Crude divorce rate'],
        color=colors[i],
        linestyle='--',
        label=f'{country} - Divorce Rate'
    )

ax2.set_ylabel('Crude Divorce Rate')
ax2.tick_params(axis='y', labelcolor='black')

# === 7. Combine legends ===
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines + lines2, labels + labels2, loc='upper left', bbox_to_anchor=(1.05, 1))

# === 8. Title & layout ===
plt.title('Working Hours vs Divorce Rate by Country')
plt.tight_layout()
plt.show()
