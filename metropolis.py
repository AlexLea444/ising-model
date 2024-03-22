import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# Function to perform Metropolis algorithm steps
def metropolis(lattice, temperature, J):
    num_rows, num_cols = lattice.shape
    for _ in range(lattice.size):
        # coordinates of site of spin flip, whose spin is lattice[x, y]
        x = np.random.randint(0, num_cols)
        y = np.random.randint(0, num_rows)

        neighbor_spin_sum = lattice[(y + 1) % N, x] + lattice[y,(x + 1) % N] + lattice[(y - 1) % N, x] + lattice[y,(x - 1) % N]
        dE = -J * lattice[y, x] * neighbor_spin_sum
        if dE < 0 or np.random.rand() < np.exp(-dE / (kB * temperature)):
            lattice[y, x] *= -1


# Function to update the animation
def animate(frame):
    metropolis(lattice, temperature, J)
    img.set_data(lattice)
    return img,


if __name__ == "__main__":
    # Define constants
    N = 50  # Size of lattice
    J = 1  # Interaction energy
    kB = 1  # Boltzmann constant
    temperature = 2.0  # Temperature
    steps = 1000000  # Number of Monte Carlo steps
    burn_in = 500  # Burn-in steps

    # Initialize lattice
    lattice = np.random.choice([-1, 1], size=(N, N))

    # Create a figure and axis object
    fig, ax = plt.subplots()

    # Initialize an empty image
    img = ax.imshow(lattice, cmap='coolwarm', interpolation='nearest')
    plt.axis('off')

    # Create animation
    ani = animation.FuncAnimation(fig, animate, frames=steps, interval=50)
    plt.show()
