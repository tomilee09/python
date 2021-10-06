# La idea es una tortuguita que avanza y deja un camino, este camino
# se queda grabado y se ve en pantalla, se le tiene que indicar donde ir 
# su direccion, su color, etc...

# Funciones principales en Turtle Graphics

# Las funciones principales para animar nuestro objeto son las siguientes:

# forward(distance): Avanzar una determinada cantidad de píxeles.
# backward(distance): Retroceder una determinada cantidad de píxeles.
# left(angle): Girar hacia la izquierda un determinado ángulo.
# right(angle): Girar hacia la derecha un determinado ángulo.

# Por otro lado, puede que en ocasiones queramos desplazarnos de un punto a otro sin dejar rastro. Para ello utilizaremos las siguientes funciones:

# home(distance): Desplazarse al origen de coordenadas.
# goto((x, y)): Desplazarse a una coordenada en concreto.
# pendown(): Subir el lápiz para no mostrar el rastro.
# penup(): Bajar el lápiz para mostrar el rastro.

# Por último, puede que queramos cambiar el color o tamaño del lápiz. En ese caso utilizaremos las siguientes funciones gráficas:

# shape(‘turtle’): Cambia al objeto tortuga.
# pencolor(color): Cambiar al color especificado.
# pensize(dimension): Tamaño de la punta del lápiz.

# MI EJEMPLO:
# import turtle

# window = turtle.Screen()
# tortuga = turtle.Turtle()

# for i in range(6):
#     tortuga.forward(100)
#     tortuga.right(60)

# window.mainloop()


# EJEMPLO SACADO DE COMENTARIO DE PLATZI
import turtle
window = turtle.Screen()
colors=['red','purple','blue','green','yellow','orange']

t = turtle.Pen()
t.speed(10)
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x/100+1)
    t.forward(x)
    t.left(59)

turtle.mainloop()