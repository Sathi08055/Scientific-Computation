import numpy as np
import matplotlib.pyplot as plt

num_points=10
a=-10
b=10
def my_function_vector(x,y):
    r=1
    #r=np.sqrt(x**2 +y**2)*2
    vx=-y
    vy=x
    return vx/r, vy/r

def my_curl(f,x,y,h=1e-5):
    fyx=(f(x+h,y)[1]-f(x-h,y)[1])/(2*h)
    fxy=(f(x,y+h)[0]-f(x,y-h)[0])/(2*h)
    cz=fyx-fxy
    return cz

x=np.linspace(a,b,num_points)
y=np.linspace(a,b,num_points)
z=np.array([1])
x_mesh,y_mesh,z_mesh =np.meshgrid(x,y,z)


z=np.array([1])

fig=plt.figure()
ax_1=fig.add_subplot(projection="3d")
vx,vy=my_function_vector(x_mesh,y_mesh)

ax_1.quiver(x_mesh,y_mesh,z_mesh,0,0,my_curl(my_function_vector,x_mesh,y_mesh),color="red")
ax_1.quiver(x_mesh,y_mesh,z_mesh,vx,vy,0,color="green")
ax_1.view_init(elev=0)
ax_1.set_zlim(0,10)
ax_1.set_xlabel("X")
ax_1.set_ylabel("Y")
plt.show()
