import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

#introducimos la funcion inicial
def funcion(x, y):
    return(x**2 + y**2)

            # CALCULAR GRADIANTE
punto = np.random.rand(2)*4
delta = 0.01

def derivada_parcial(punto):
    return (funcion(punto[0]+delta, punto[1]+delta) - funcion(punto[0], punto[1]))/delta

def gradiante(punto):
    gradiante = np.zeros(2) # creo un vector con 2 componentes con valores cero
    gradiante[0] = (funcion(punto[0]+delta, punto[1]) - funcion(punto[0], punto[1]))/delta
    gradiante[1] = (funcion(punto[0], punto[1]+delta) - funcion(punto[0], punto[1]))/delta
    return gradiante



            # HACER DESCENSO DE GRADIANTE

pasos = 100
learning_rate = 0.1
lista_puntos = list([]) # esto es solo para graficarlos
for i in range(pasos):
    punto = punto - gradiante(punto)*learning_rate
    lista_puntos.append(punto)

            # GRAFICAR DESCENSO DE GRADIANTE
resolucion = 100

#creamos unas listas con puntos pa graficar
x = np.linspace(-4, 4, resolucion)
y = np.linspace(-4, 4, resolucion)

#creamos toda la malla con los anteriores puntos
x,y = np.meshgrid(x,y)

#creamos un entorno 3d con matplotlib
fig , ax = plt.subplots(subplot_kw={"projection":"3d"})

#al entorno 3d le ponemos una superficie
superficie = ax.plot_surface(x,y,funcion(x, y))

# graficamos los puntos
for i in range(pasos):
    ax.scatter3D(lista_puntos[i][0], lista_puntos[i][1], funcion(lista_puntos[i][0], lista_puntos[i][1]))

plt.show()

print(lista_puntos[pasos-1])