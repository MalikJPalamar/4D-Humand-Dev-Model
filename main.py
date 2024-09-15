import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

# Parameters for the lattice and iceberg
lattice_size = 10
iceberg_base_size = 3
iceberg_top_size = 1.5
iceberg_height = 2
submerged_ratio = 0.75

# Creating the figure and axis
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')


# Function to draw the lattice lines
def draw_lattice(ax, size):
  # Lattice lines along X and Y at Z=0
  for i in np.linspace(-size, size, num=int(size * 2 + 1)):
    ax.plot([i, i], [-size, size], [0, 0],
            color='grey',
            linestyle=':',
            linewidth=0.5)
    ax.plot([-size, size], [i, i], [0, 0],
            color='grey',
            linestyle=':',
            linewidth=0.5)


# Function to draw the iceberg, corrected to properly form faces
def draw_iceberg(ax, base_size, height, submerged_ratio):
  tip_height = height * (1 - submerged_ratio)
  base_height = -height * submerged_ratio

  # Top vertices of the iceberg
  top_vertices = np.array([
      [base_size, base_size, tip_height],
      [-base_size, base_size, tip_height],
      [-base_size, -base_size, tip_height],
      [base_size, -base_size, tip_height],
      [base_size, base_size, tip_height]  # Close the loop
  ])

  # Bottom vertices of the iceberg
  bottom_vertices = np.array([
      [base_size, base_size, base_height],
      [-base_size, base_size, base_height],
      [-base_size, -base_size, base_height],
      [base_size, -base_size, base_height],
      [base_size, base_size, base_height]  # Close the loop
  ])

  # Faces of the iceberg
  faces = [[
      top_vertices[i], top_vertices[i + 1], bottom_vertices[i + 1],
      bottom_vertices[i]
  ] for i in range(4)]
  faces.append([top_vertices[i] for i in range(4)])  # Top face
  faces.append([bottom_vertices[i] for i in range(4)])  # Bottom face

  # Create the 3D polygons for the faces and add them to the plot
  poly3d = Poly3DCollection(faces,
                            facecolors='cyan',
                            linewidths=1,
                            edgecolors='black',
                            alpha=0.5)
  ax.add_collection3d(poly3d)


# Function to draw the horizontal plane (Z=0)
def draw_horizontal_plane(ax, size):
  # Points defining the horizontal plane
  x = np.array([-size, size])
  y = np.array([-size, size])
  X, Y = np.meshgrid(x, y)
  Z = np.zeros_like(X)
  ax.plot_surface(X, Y, Z, color='gray', alpha=0.1)


# Function to draw the vertical plane (Y=0) based on the provided endpoints
def draw_vertical_plane(ax, size, height):
  # Points defining the vertical plane
  X, Z = np.meshgrid([size, -size], [0, height])
  Y = np.zeros_like(X)
  ax.plot_surface(X, Y, Z, color='gray', alpha=0.1)


# Draw the lattice, iceberg, and both planes
draw_lattice(ax, lattice_size)
draw_iceberg(ax, iceberg_base_size, iceberg_height, submerged_ratio)
draw_horizontal_plane(ax, lattice_size)
draw_vertical_plane(ax, -lattice_size, iceberg_height * (1 - submerged_ratio))

# Set the axes labels and limits
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

# Set the axes limits
ax.set_xlim([-lattice_size, lattice_size])
ax.set_ylim([-lattice_size, lattice_size])
ax.set_zlim([-iceberg_height * submerged_ratio, iceberg_height])

# Set the viewing angle for better visualization
ax.view_init(30, 45)

# Show the plot
plt.show()
