import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

# 1. Load data and clean column names
df = pd.read_csv('distance.csv')
df.columns = df.columns.str.strip()

# 2. Print column names for debugging
print("Columns found in CSV:", df.columns.tolist())

# 3. Check for required columns
required_cols = {'X', 'Y', 'Z'}
if not required_cols.issubset(df.columns):
    raise ValueError(f"CSV must contain columns: {required_cols}")

# 4. Convert columns to numeric, coerce errors to NaN
for col in ['X', 'Y', 'Z']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# 5. Drop rows with any NaN values in X, Y, or Z
df = df.dropna(subset=['X', 'Y', 'Z'])

# 6. Extract data
x = df['X'].values
y = df['Y'].values
z = df['Z'].values

# 7. Create grid for interpolation
xi = np.linspace(x.min(), x.max(), 10)
yi = np.linspace(y.min(), y.max(), 10)
xi, yi = np.meshgrid(xi, yi)

# 8. Interpolate Z values onto grid
zi = griddata((x, y), z, (xi, yi), method='cubic')

# 9. Plot contour
plt.figure(figsize=(8, 6))
contour = plt.contourf(yi, xi, zi, levels=50, cmap='turbo')
plt.colorbar(contour, label='Z value')
plt.xlabel('R(Å)')
plt.ylabel('Z(Å)')
plt.title('Contour Plot from CSV Data')
plt.show()
