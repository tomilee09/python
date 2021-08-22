import pandas as pd
import numpy as np
import scipy
import scipy.stats
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('bicicletas-compartidas.csv')
y = df['bicis-compartidas']

# podemos ver los percentiles de los datos
print(np.percentile(y, q=50))

# podemos ver varios percentiles de una
# cuartiles
print(np.percentile(y, q=[0, 25, 50, 75, 100]))

# quintiles
print(np.percentile(y, q=[0, 20, 40, 60, 80, 100]))

# deciles
print(np.percentile(y, q=np.arange(0, 110, 10)))

# podemos hacer esto mas rapido 
print(y.describe())

# podemos hacer un histograma con matplotlib (bins son la cantidad de divisiones)
plt.hist(y, bins = 300)
plt.show()

# una buena parte para graficar con plt es subplots
z = df['viento']
fig, ax = plt.subplots()
ax.pie(z.value_counts())
plt.show()

# podemos hacer un boxplot con sns
sns.boxplot(x=y)
plt.show()

# podemos graficar una nube de puntos creada por z y y, ademas alpha es un parametro que modifica la transparencia de los puntos, por lo que permite ver mejor donde es la concentracion de puntos
plt.scatter(z, y, alpha = 0.03)
plt.show()

# dato extra: se puede hacer una media ponderada
print(np.mean(y))
print(np.mean(z))
print(np.average(z, weights = y))
print(np.average(y, weights = z))