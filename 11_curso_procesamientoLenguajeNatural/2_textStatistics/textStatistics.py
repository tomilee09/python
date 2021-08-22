import nltk
import re
# previamente descargamos el conjunto de textos llamado 'book'
from nltk.book import *
import matplotlib.pyplot as plt
import numpy as np

# book tiene muchos libros, vamos a usar text1 que en realidad es Moby Dick
# veamos cuantos tokens tiene
print(len(text1.tokens)) # len(text1) = len(text1.tokens)

# ahora veamos cuantas palabras unicas tiene (es decir todo el vocabulario ndel texto)
vocabulario = sorted(set(text1)) # sorted es para ordenar alfabeticamente y set es para obtener una lista de elementos no repetidos
print(len(vocabulario))

# con lo anterior podemos calcular muchas cosas, como por ejemplo la riqueza lexica
def riqueza_lexica(texto):
    vocabulario = sorted(set(texto))
    return len(vocabulario)/len(texto)
print(riqueza_lexica(text1))

# o el porcentaje de aparición de una palabra
def porcentaje_palabra(palabra, texto):
    return 100*texto.count(palabra)/len(texto)
print(porcentaje_palabra('monster', text1))

# Además podemos hacer una distribucion de frecuencias de las palabras que tenemos con FrecDist()
frecuencia = FreqDist(text1)

# podemos mostrar los tokens mas comunes
frecuencia.most_common(20)

# y podemos graficar los mas comunes facilmente
frecuencia.plot(40)

# para no mostrar las comas, puntos, o conectores en general (como por ejemplo 'the') vamos a filtrar las palabras, set(text1 va a hacer que las palabras no se repitan)
palabras_filtradas = [palabra for palabra in set(text1) if len(palabra)>5]

#creamos un vocabulario con estas palabras
vocabulario_filtrado = sorted(set(palabras_filtradas))

#podemos crear un array a partir de las frecuencias que ya tenemos de las palabras
palabras_y_frecuencias = [(palabra, frecuencia[palabra]) for palabra in palabras_filtradas if frecuencia[palabra]>10]

# ahora convertimos
dtypes = [('palabra', 'S10'), ('frecuencia', int)] # S10 es un formato para los strings
palabras_y_frecuencias = np.array(palabras_y_frecuencias, dtype = dtypes)

# ahora que ya lo convertimos a un numpy array los ordenamos
palabras_y_frecuencias_ordenado = np.sort(palabras_y_frecuencias, order = 'frecuencia')

# ahora graficamos
numero = 200
palabras_y_frecuencias_ordenado_graficar = palabras_y_frecuencias_ordenado[-numero:]
x = palabras_y_frecuencias_ordenado_graficar['palabra']
y = palabras_y_frecuencias_ordenado_graficar['frecuencia']
plt.plot(x, y)
plt.xticks(x, rotation = 'vertical')
plt.grid(True)
plt.show()
