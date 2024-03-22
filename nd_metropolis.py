import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# Function to perform Metropolis algorithm steps
def nd_metropolis(lattice, temperature, J):
    dimensions = lattice.shape
    for _ in range(lattice.size):
        # coordinates of site of spin flip, whose spin is lattice[x, y]
        coordinates = [np.random.randint(0, dim) for dim in dimensions]

        neighbor_spin_sum = 0
        for dim, n_coord in enumerate(coordinates):
            coordinates[dim] = (n_coord - 1) % dimensions[dim]
            neighbor_spin_sum += lattice[tuple(coordinates)]
            coordinates[dim] = (n_coord + 1) % dimensions[dim]
            neighbor_spin_sum += lattice[tuple(coordinates)]
            coordinates[dim] = n_coord

        dE = -J * lattice[tuple(coordinates)] * neighbor_spin_sum
        if dE < 0 or np.random.rand() < np.exp(-dE / (kB * temperature)):
            lattice[tuple(coordinates)] *= -1


# Function to update the animation
def update(frame):
    nd_metropolis(lattice, temperature, J)
    # Choose a random 'layer' to reduce lattice to two dimensions for display
    img.set_data(lattice[display_layer])
    return img,


if __name__ == "__main__":
    # Define constants
    J = 1  # Interaction energy
    kB = 1  # Boltzmann constant
    width = 10  # Width of lattice
    dims = 6  # Number of dimensions
    temperature = 2.0  # Temperature
    steps = 1000000  # Number of Monte Carlo steps
    burn_in = 500  # Burn-in steps

    # Initialize lattice
    lattice = np.random.choice([-1, 1], size=tuple([width for x in range(dims)]))

    # Create a figure and axis object
    fig, ax = plt.subplots()

    # Initialize display
    ax.set_title(f'{len(lattice.shape)}D Lattice')
    print([np.random.randint(0, dim) for dim in lattice.shape][:-2])

    # To represent n-dim lattice as 2D, choose a random layer for display
    random_layer = [np.random.randint(0, dim) for dim in lattice.shape][:-2]
    display_layer = tuple(random_layer)

    img = ax.imshow(lattice[display_layer], cmap='coolwarm', interpolation='nearest')
    plt.axis('off')

    # Create animation
    ani = animation.FuncAnimation(fig, update, frames=steps, interval=50)

    # Show the animation
    plt.show()
