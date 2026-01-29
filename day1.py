import numpy as np
import pyvista as pv

x=np.array([1,2,4])
y=np.array([7,8,6])
z=np.array([0])
x,y,z=np.meshgrid(x,y,z)
points=np.column_stack((x.ravel(),y.ravel(),z.ravel()))

def vector(r=points):
    x=r[:,0]
    y=r[:,1]
    u=-y
    v=x
    vec= np.column_stack((u,v,np.zeros(u.shape)))
    return vec
field=pv.PolyData(points)
field['vectors']=vector()

arrows = field.glyph(
    orient="vectors",
    scale=False,
    factor=0.35,)

plotter = pv.Plotter()
plotter.add_mesh(arrows, color="royalblue")
plotter.add_axes()
plotter.view_xy()
plotter.show()