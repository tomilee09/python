import numpy as np
import matplotlib.pyplot as plt

numero_datos = int(input("cuantos datos?: "))
x = np.array(list(range(numero_datos)))
y = np.array([i * i for i in range(numero_datos)])

coeficientes = np.polyfit(x, y, 1)
print(coeficientes)

a = coeficientes[0]
b = coeficientes[1]
funcion = (a * x) + b

plt.plot(x, funcion)
plt.scatter(x, y)
plt.show()


