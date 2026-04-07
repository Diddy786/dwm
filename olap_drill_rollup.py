import pandas as pd

# Sample dataset
data = {
    'Year': [2022, 2022, 2023, 2023],
    'Region': ['North', 'South', 'North', 'South'],
    'Sales': [100, 200, 150, 300]
}
df = pd.DataFrame(data)

print("Original Data:")
print(df)

# -------- ROLL-UP --------
rollup = df.groupby('Year')['Sales'].sum()
print("\nRoll-Up (Sales by Year):")
print(rollup)

# -------- DRILL-DOWN --------
drilldown = df.groupby(['Year', 'Region'])['Sales'].sum()
print("\nDrill-Down (Sales by Year and Region):")
print(drilldown)
