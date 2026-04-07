# 5. Slice and Dice (OLAP)

```python
import pandas as pd

data = {'Region': ['North', 'South', 'East', 'West', 'North'],
        'Product': ['A', 'B', 'A', 'B', 'A'],
        'Sales': [100, 200, 150, 300, 250]}
df = pd.DataFrame(data)
print("Original Data:")
print(df)

# -------- SLICE --------
slice_data = df[df['Product'] == 'A']
print(slice_data)

# -------- DICE --------
dice_data = df[(df['Product'] == 'A') & (df['Region'] == 'North')]
print(dice_data)
```

---

# 6. Drill-Down and Roll-Up (OLAP)

```python
import pandas as pd

data = {'Year': [2022, 2022, 2023, 2023],
        'Region': ['North', 'South', 'North', 'South'],
        'Sales': [100, 200, 150, 300]}
df = pd.DataFrame(data)
print("Original Data:")
print(df)

# -------- ROLL-UP --------
rollup = df.groupby('Year')['Sales'].sum()
print(rollup)

# -------- DRILL-DOWN --------
drilldown = df.groupby(['Year', 'Region'])['Sales'].sum()
print(drilldown)
```
