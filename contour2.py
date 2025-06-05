import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('distance.csv')

# Pivot the data to create a grid for contour plotting
pivot = df.pivot_table(index='Z', columns='R', values='Energy')

# Create meshgrid for contour plot
R = pivot.columns.values
Z = pivot.index.values
R_grid, Z_grid = np.meshgrid(R, Z)
Energy_grid = pivot.values

# Plot filled contour
plt.figure(figsize=(8,6))
contour = plt.contourf(R_grid, Z_grid, Energy_grid, levels=np.linspace(0,2,50), cmap='viridis')
plt.xlabel('R(Å)')
plt.ylabel('Z(Å)')
plt.title('Filled Contour Plot of Energy')
plt.colorbar(contour, label='Energy(eV)')
plt.show()
