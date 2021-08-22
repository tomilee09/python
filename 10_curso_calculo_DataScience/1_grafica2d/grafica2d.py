#Grafica 3D
from matplotlib import cm       #Para colores 
import numpy as np              #Para crear lo arreglos y las funciones matematicas 
import matplotlib.pyplot as plt #Para graficar 
def z(x,y):
  return np.sin(x) + 2 * np.cos(y)
res = 10
x = np.linspace(-4,4,num=res)
y = np.linspace(-4,4,num=res)
x,y = np.meshgrid(x,y)
z = z(x,y)

fig , ax = plt.subplots(subplot_kw={"projection":"3d"})
surf = ax.plot_surface(x,y,z,cmap=cm.cool)
fig.colorbar(surf)
plt.show()