import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from scipy.stats import norm

def gaussian(x, media, desviacion):
    return 1/(desviacion * np.sqrt(2*np.pi))*np.exp(-0.5*((x-media)/desviacion)**2)

x = np.arange(-4, 4, 0.1)
y = gaussian(x, 0, 1)

plt.plot(x, y)
plt.show()

distribucionGaussiana = norm(0, 1)
x2 = np.arange(-4, 4, 0.1)
y2 = [distribucionGaussiana.pdf(value) for value in x2] 
#pdf es probability distribution function

plt.plot(x2, y2)
plt.show()

# veamos algunos valores de la distribucion de probabilidad (ojo: valor de la dist. de probabilidad es distinto al valor de la probabilidad, solo se puede hacer la igualdad con los intervalos (el valor acumulado))
print(distribucionGaussiana.pdf(0))

# ahora veamos el valor de la probabilidad acumulada
print(distribucionGaussiana.cdf(0))

# ahora importamos datos con comportamiento gaussiano y comprobamos esto
df = pd.read_excel('datos.xls')
tamano_alas = df['Normally Distributed Housefly Wing Lengths'].values[4:]
#np.unique cuenta cuantas veces se repite un valor
valores_tamano_alas, repeticion = np.unique(tamano_alas, return_counts=True)
plt.bar(valores_tamano_alas, repeticion)
plt.show()

# ahora que tenemos la grafica de los datos vamos a buscar la distribucion que se parezca
# buscar el promedio
mu = tamano_alas.mean()
sigma = tamano_alas.std()
distribucion_encontrada = norm(mu, sigma)
x = np.arange(30, 60, 0.1)
y = [distribucion_encontrada.pdf(i) for i in x]
plt.plot(x, y)
plt.bar(valores_tamano_alas, repeticion/len(tamano_alas))
plt.show()