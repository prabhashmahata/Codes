import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter

# Load data
data = np.loadtxt("en.dat")
time = data[:, 0]
energies = data[:, 1:]

# Convert au → eV
energies *= 27.2114

# Number of energy columns
n_cols = energies.shape[1]

# Custom labels and styles
labels = []
styles = []

for i in range(n_cols):
    if i < 4:
        labels.append(f'state{i+1}')
        styles.append('-')
    elif i == 4:
        labels.append("Current state")
        styles.append('.')
    elif i == 5:
        labels.append("Total energy")
        styles.append('--')
    else:
        labels.append(f'Unknown{i}')
        styles.append('-')

# Plot setup
fig, ax = plt.subplots(figsize=(10, 6))
lines = [ax.plot([], [], styles[i], label=labels[i], lw=2)[0] for i in range(n_cols)]

ax.set_xlim(time[0], time[-1])
ax.set_ylim(np.min(energies), np.max(energies))
ax.set_xlabel("Time")
ax.set_ylabel("Energy (eV)")
ax.set_title("Energy vs Time (in eV)")
# Remove grid
# ax.grid(True)  ← Disabled
# Fixed legend in top-right
ax.legend(loc='upper right')

# Animation functions
def init():
    for line in lines:
        line.set_data([], [])
    return lines

def update(frame):
    for i, line in enumerate(lines):
        line.set_data(time[:frame+1], energies[:frame+1, i])
    return lines

# Animate and save as MP4
ani = FuncAnimation(fig, update, frames=len(time), init_func=init, blit=True, interval=100)
writer = FFMpegWriter(fps=10)
ani.save("energy_animation_eV.mp4", writer=writer)

print("✅ Saved as 'energy_animation_eV.mp4'")
