import numpy as np
import matplotlib.pyplot as plt

# Grid size
nx, ny = 60, 60
dx, dy = 1.0, 1.0
dt = 0.05
viscosity = 0.1

# Velocity fields
u = np.ones((ny, nx))   # x-direction velocity
v = np.zeros((ny, nx))  # y-direction velocity

# Simulation loop
for n in range(500):
    un = u.copy()
    vn = v.copy()

    # Update velocities using simplified Navier-Stokes
    u[1:-1, 1:-1] = (
        un[1:-1, 1:-1]
        - dt * (un[1:-1, 1:-1] * (un[1:-1, 1:-1] - un[1:-1, :-2]) / dx +
                vn[1:-1, 1:-1] * (un[1:-1, 1:-1] - un[:-2, 1:-1]) / dy)
        + viscosity * (
            (un[1:-1, 2:] - 2 * un[1:-1, 1:-1] + un[1:-1, :-2]) / dx**2 +
            (un[2:, 1:-1] - 2 * un[1:-1, 1:-1] + un[:-2, 1:-1]) / dy**2
        )
    )

    v[1:-1, 1:-1] = (
        vn[1:-1, 1:-1]
        - dt * (un[1:-1, 1:-1] * (vn[1:-1, 1:-1] - vn[1:-1, :-2]) / dx +
                vn[1:-1, 1:-1] * (vn[1:-1, 1:-1] - vn[:-2, 1:-1]) / dy)
        + viscosity * (
            (vn[1:-1, 2:] - 2 * vn[1:-1, 1:-1] + vn[1:-1, :-2]) / dx**2 +
            (vn[2:, 1:-1] - 2 * vn[1:-1, 1:-1] + vn[:-2, 1:-1]) / dy**2
        )
    )

    # 🔴 Apply boundary conditions (VERY IMPORTANT)

    # Inlet (left side)
    u[:, 0] = 1
    v[:, 0] = 0

    # Outlet (right side - simple)
    u[:, -1] = u[:, -2]
    v[:, -1] = v[:, -2]

    # Top & bottom walls
    u[0, :] = 1
    u[-1, :] = 1
    v[0, :] = 0
    v[-1, :] = 0

    # 🔴 Obstacle (square in center)
    u[25:35, 25:35] = 0
    v[25:35, 25:35] = 0

# 🔵 Visualization (BEST VIEW)
speed = np.sqrt(u**2 + v**2)

plt.figure(figsize=(6,6))
plt.imshow(speed, cmap='jet')
plt.colorbar(label='Velocity Magnitude')

# Draw obstacle
plt.gca().add_patch(plt.Rectangle((25,25),10,10,color='black'))

plt.title("2D CFD Flow Around Obstacle")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()