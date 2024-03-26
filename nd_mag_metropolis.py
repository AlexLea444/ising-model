import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def nd_magnetization(lattice):
    return np.sum(lattice) / lattice.size


# Function to perform Metropolis algorithm steps
def nd_metropolis(lattice, temperature, J):
    net_spin_change = 0
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

        dE = J * lattice[tuple(coordinates)] * neighbor_spin_sum
        if dE < 0 or np.random.rand() < np.exp(-dE / (kB * temperature)):
            lattice[tuple(coordinates)] *= -1
            net_spin_change += lattice[tuple(coordinates)]
    return net_spin_change * 2 / lattice.size


# Function to update the animation
def update(frame):
    magnetization[frame] = magnetization[frame - 1] + nd_metropolis(lattice, temperature, J)
    # Choose a random 'layer' to reduce lattice to two dimensions for display
    img.set_data(lattice[display_layer])
    return img,


if __name__ == "__main__":
    # Define constants
    J = -1  # Interaction energy
    kB = 1  # Boltzmann constant
    width = 10  # Width of lattice
    dims = 2  # Number of dimensions
    temperature = 0.1  # Temperature
    steps = 10000  # Number of Monte Carlo steps
    magnetization = 0

    # Initialize lattice
    lattice = np.random.choice([-1, 1], size=tuple([width for x in range(dims)]))
    magnetization = np.zeros(steps)
    magnetization[0] = nd_magnetization(lattice)

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

    plt.plot(magnetization)
    plt.xlabel('Steps')
    plt.ylabel('Magnetization')
    plt.suptitle('Magnetization Value over Time')
    plt.show()
