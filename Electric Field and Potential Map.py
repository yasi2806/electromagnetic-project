import numpy as np
import matplotlib.pyplot as plt

k_e = 8.99e9
q = float(input("q (Example: 1e-9) :  "))
width, height = int(input("width: ")), int(input("height: "))
num_points = 100

x = np.linspace(-width / 2, width / 2, num_points)
y = np.linspace(-height / 2, height / 2, num_points)
X, Y = np.meshgrid(x, y)

R = np.sqrt(X**2 + Y**2)
R[R == 0] = np.nan

Ex = k_e * q * X / R**3
Ey = k_e * q * Y / R**3

V = k_e * q / R

fig, ax = plt.subplots(1, 2, figsize=(14, 6))

ax[0].quiver(X, Y, Ex, Ey, scale=20, color='blue')
ax[0].set_title('Electric Field')
ax[0].set_xlabel('X (meters)')
ax[0].set_ylabel('Y (meters)')
ax[0].axis('equal')

contour = ax[1].contourf(X, Y, V, 20, cmap='inferno')
ax[1].set_title('Electric Potential')
ax[1].set_xlabel('X (meters)')
ax[1].set_ylabel('Y (meters)')
fig.colorbar(contour, ax=ax[1])

plt.tight_layout()
plt.show()
