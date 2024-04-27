
import numpy as np
import matplotlib.pyplot as plt

v_BA_vector = np.array([0, -30])  # B's movement is downwards (south) from A's perspective
v_CA_vector = np.array([30, 0])   # C's movement is to the right (east) from A's perspective

# Define the vector for B relative to C, which is the sum of B relative to A and A relative to C (which is just -C relative to A)
v_BC_vector = v_BA_vector - v_CA_vector

# Create a new figure for the graph
fig, ax = plt.subplots()

# Draw the vectors
ax.quiver(0, 0, v_BA_vector[0], v_BA_vector[1], angles='xy', scale_units='xy', scale=1, color='red', label='Plate B relative to A')
ax.quiver(0, 0, v_CA_vector[0], v_CA_vector[1], angles='xy', scale_units='xy', scale=1, color='green', label='Plate C relative to A')
ax.quiver(v_CA_vector[0], v_CA_vector[1], v_BC_vector[0], v_BC_vector[1], angles='xy', scale_units='xy', scale=1, color='blue', label='Plate B relative to C')

# Set the axes limits
ax.set_xlim(-40, 40)
ax.set_ylim(-40, 40)

# Add grid, legend, and labels
ax.grid(True)
ax.legend()
ax.set_aspect('equal', adjustable='box')
ax.set_title('Velocity Vectors at Triple Junction')
ax.set_xlabel('Velocity in mm/yr (East-West)')
ax.set_ylabel('Velocity in mm/yr (North-South)')

# Show the plot
plt.show()