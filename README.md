# DWM Practicals

## 📥 [Download Offline Version (HTML)](https://github.com/Diddy786/dwm/raw/main/practical.html)

Right-click the link above → Save Link As → Open the downloaded HTML file in any browser (works offline)

---

# Practical No. 2: Install Device Drivers

## a) Install and Configure Hardware Device Drivers on Windows Server

1. Right-click Start. Click Device Manager

2. Identify Devices Needing Drivers

3. for Automatic Installation:

Right-click the device → Update Driver.

![Update Driver](1.png)

Choose Search automatically for drivers.

![Search automatically](2.png)

Windows checks Windows Update or preloaded drivers.

For Manual Installation:
- Download the latest driver from the vendor website.
- Right-click the device → Update Driver → Browse my computer for drivers.
- Select the downloaded driver folder → Install.

4. To Configure the Driver Right-click the device. Click Properties. Configure settings under tabs: Driver (update, roll back, disable), Power Management, Advanced (device-specific settings)

5. Restart the Server (if needed)

**Uninstall Device Drivers**

1. Right-click Start. Select Device Manager
2. Locate the Device.
3. Open Device Properties. Right-click the device.

![Device Properties](3.png)

Click Properties

4. In the Properties window → click Driver tab. Click Uninstall

![Uninstall Driver](4.png)

5. Restart the Server

---

# 5. Slice and Dice (OLAP)

Step 1 — Install the pandas library:

```bash
pip install pandas
```

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

Step 1 — Install the pandas library:

```bash
pip install pandas
```

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
