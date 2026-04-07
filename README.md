# OLAP Operations in Python

OLAP (Online Analytical Processing) operations using pandas.

---

## 5. Slice and Dice

**Slice** — filter on one dimension. **Dice** — filter on multiple dimensions.

```python
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
```

---

## 6. Drill-Down and Roll-Up

**Roll-Up** — aggregate to a higher level. **Drill-Down** — break down to a lower level.

```python
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
```

---

## How to Run

```bash
pip install pandas
python olap_slice_dice.py
python olap_drill_rollup.py
```
