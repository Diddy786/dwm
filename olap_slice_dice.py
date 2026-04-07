import pandas as pd

# Sample dataset
data = {
    'Region': ['North', 'South', 'East', 'West', 'North'],
    'Product': ['A', 'B', 'A', 'B', 'A'],
    'Sales': [100, 200, 150, 300, 250]
}
df = pd.DataFrame(data)

print("Original Data:")
print(df)

# -------- SLICE --------
slice_data = df[df['Product'] == 'A']
print("\nSliced Data (Product == 'A'):")
print(slice_data)

# -------- DICE --------
dice_data = df[(df['Product'] == 'A') & (df['Region'] == 'North')]
print("\nDiced Data (Product == 'A' AND Region == 'North'):")
print(dice_data)
