import pandas as pd
import numpy as np
import scipy
import scipy.stats
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('bicicletas-compartidas.csv')

y = df['bicis-compartidas']

# la profe dijo que habia quitar los 0's
y = np.where(y==0, 1, y)


# promedio
print(np.mean(y))

# media geometrica
print(scipy.stats.mstats.gmean(y))

# media armonica
print(scipy.stats.mstats.hmean(y))

# mediana
print(np.median(y))
x = [1, 0, 10, 1]

# moda 
print(scipy.stats.mode(x).mode)

# desviacion estandar
print(np.std(y))

# podemos hacer copias con .copy()
y_alterado = y.copy()

# podemos graficar los datos como una caja de bigotes de gato
sns.boxplot(x=y) # advertencia: se ve feo por los datos, no es un error
plt.show()

# y tenemos mas graficas
sns.distplot(y)
plt.show()