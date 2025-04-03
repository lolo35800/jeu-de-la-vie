import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Dimensions de la grille
N = 100

# Initialisation aléatoire de la grille
grid = np.random.choice([0, 1], N*N, p=[0.8, 0.2]).reshape(N, N)

def update(frameNum, img, grid, N):
    # Copie de la grille pour appliquer les règles
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):
            # Calcul du nombre de voisins vivants
            total = int((grid[i, (j-1)%N] + grid[i, (j+1)%N] +
                         grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                         grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +
                         grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N]))

            # Application des règles
            if grid[i, j] == 1:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = 0
            else:
                if total == 3:
                    newGrid[i, j] = 1

    # Mise à jour de la grille
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,

# Configuration de l'affichage
fig, ax = plt.subplots()
img = ax.imshow(grid, interpolation='nearest')
ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N, ),
                              frames=10,
                              interval=200,
                              save_count=50)

plt.show()
