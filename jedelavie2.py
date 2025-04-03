import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Dimensions de la grille
N = 100

# Initialisation de la grille avec le canon à planeur
grid = np.zeros(N*N).reshape(N, N)

# Configuration du canon à planeur
glider_gun = [
    (5, 1), (5, 2), (6, 1), (6, 2), (5, 11), (6, 11), (7, 11),
    (4, 12), (3, 13), (3, 14), (8, 12), (9, 13), (9, 14),
    (6, 15), (4, 16), (5, 17), (6, 17), (7, 17), (6, 18),
    (8, 16), (3, 21), (4, 21), (5, 21), (3, 22), (4, 22),
    (5, 22), (2, 23), (6, 23), (1, 25), (2, 25), (6, 25),
    (7, 25), (3, 35), (4, 35), (3, 36), (4, 36)
]

# Placement du canon à planeur sur la grille
for x, y in glider_gun:
    grid[x + 10, y + 30] = 1  # Décalage pour centrer le canon à planeur

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
