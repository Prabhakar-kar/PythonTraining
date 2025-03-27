import math
import matplotlib.pyplot as plt

# Get user input
v_0 = input("Enter initial velocity values (comma-separated): ")
v_0_list = [float(v) for v in v_0.split(",")]

# Constants
angle = 45  # degrees
g = 9.8  # m/s^2
angle_rad = math.radians(angle)
sin_45 = math.sin(angle_rad)  

# Calculate max height for each velocity
h_max_list = [((v * sin_45) ** 2) / (2 * g) for v in v_0_list]

# Print results
print("Initial velocity (v0):", v_0_list)
print("Max height (m):", h_max_list)

# Plot the graph
plt.plot(v_0_list, h_max_list, marker='o', linestyle='-')  
plt.xlabel("Initial Velocity (m/s)")
plt.ylabel("Max Height (m)")
plt.title("Maximum Height vs Initial Velocity")
plt.grid(True)
plt.show()
