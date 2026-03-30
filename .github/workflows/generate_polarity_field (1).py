import pyvista as pv
import numpy as np

# Create a simple 3D structured grid
x = np.linspace(-5, 5, 100)  # X-coordinates
y = np.linspace(-5, 5, 100)  # Y-coordinates
z = np.linspace(-5, 5, 100)  # Z-coordinates

# Create a 3D mesh grid
grid = pv.StructuredGrid(*np.meshgrid(x, y, z, indexing='ij'))

# Generate a scalar field using a mathematical function
# Example function: Scalar field dependent on x, y, and z.
grid['PolarityField'] = grid.points[:, 0] * grid.points[:, 1] - grid.points[:, 2] ** 2

# Set up PyVista plotter
plotter = pv.Plotter()
plotter.add_mesh(grid.sample(0.1), scalars='PolarityField', cmap='coolwarm', show_edges=False)

# Show the color bar
plotter.add_scalar_bar(title="Polarity Field μ(x)")

# Export visualization to a static image
plotter.screenshot("polarity_field.png")

# Optional: Save for interactive web embedding
plotter.export_vtkjs("polarity_field.vtkjs")

# Display interactive plot in a Python session (for verification)
plotter.show()