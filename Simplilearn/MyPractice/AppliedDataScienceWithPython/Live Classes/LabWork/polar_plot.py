import matplotlib.pyplot as plt
import numpy as np

# Generate data for a polar plot
theta = np.linspace(0, 2 * np.pi, 100)
r = theta * 2

# Create a polar plot
plt.polar(theta, r, label='Polar plot')

# Add a legend
plt.legend()

# Show the plot
plt.show()
