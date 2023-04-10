import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist, squareform

# Generate soil fungal community and soil physiochemical properties data
np.random.seed(123)
depths = ['Depth 1', 'Depth 2', 'Depth 3', 'Depth 4']

fungal_community = pd.read_csv('fungal_community.csv', header=0).values #header=None if there is no header
physiochemical_props = pd.read_csv('physiochemical_props.csv', header=0).values

# Calculate Bray-Curtis distance between fungal community data for each depth level
distances = []
for i in range(4):
    d = pdist(fungal_community[:, i].reshape(-1, 1), metric='braycurtis')
    distances.append(squareform(d))

# Plot scatter plot with four subplots, one for each depth level
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))
for i, ax in enumerate(axes.flat):
    ax.imshow(distances[i], cmap='Reds', origin='lower')
    ax.set_title(depths[i])
    ax.set_xlabel('Fungal community')
    ax.set_ylabel('Soil physiochemical properties')

plt.tight_layout()
plt.show()
