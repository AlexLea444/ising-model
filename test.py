import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Generate some sample data
x = np.linspace(0, 10, 50)
y = np.linspace(0, 10, 50)
z = np.linspace(0, 10, 50)
X, Y, Z = np.meshgrid(x, y, z)
data = np.sin(X) + np.cos(Y) + np.tan(Z)

# Create the figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Initialize scatter plot
scatter = ax.scatter(X, Y, Z, c=data.flatten(), cmap='viridis')

# Set labels and title
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.set_title('3D Heatmap')

# Update function for animation
def update(frame):
    ax.clear()
    scatter = ax.scatter(X, Y, Z, c=data.flatten(), cmap='viridis')
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    ax.set_title('3D Heatmap Frame {}'.format(frame))
    return scatter,

# Create animation
ani = FuncAnimation(fig, update, frames=range(50), interval=200)

# Show the animation
plt.show()

