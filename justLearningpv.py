import numpy as np
import pyvista as pv

# -----------------------------------
# Define vector field
# F = (-y, x, 0)
# -----------------------------------

def vector_field(x, y):
    u = -y
    v = x
    w = np.zeros_like(x)
    return np.column_stack((u, v, w))

# -----------------------------------
# Sample points (keep sparse)
# -----------------------------------

x = np.linspace(-2, 2, 12)
y = np.linspace(-2, 2, 12)
X, Y = np.meshgrid(x, y)

points = np.column_stack((
    X.ravel(),
    Y.ravel(),
    np.zeros(X.size)
))

vectors = vector_field(points[:,0], points[:,1])

vectors /= np.linalg.norm(vectors, axis=1)[:, None]



field = pv.PolyData(points)
field["vectors"] = vectors



arrows = field.glyph(
    orient="vectors",
    scale=False,
    factor=0.35,
)


plotter = pv.Plotter()
plotter.add_mesh(arrows, color="royalblue")
plotter.add_axes()
plotter.view_xy()
plotter.show()
