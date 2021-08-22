import nltk
from nltk.book import *
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px

# para encontrar colocaciones del lenguaje nos servirá aprender sobre n-gramas
# un n-grama es una consecucion de n palabras
# creemos bigramas 
bigramas = list(bigrams(text1))

# podemos ver la frecuencia de los bigramas
frecuencias = FreqDist(bigramas)

# y podemos plotear esta info
frecuencias.plot(10)

# ahora filtramos los bigramas
cota = 2
bigramas_filtrados = [bigrama for bigrama in bigramas if len(bigrama[0])>cota and len(bigrama[1])>cota]
frecuencias_bigramas_filtrados = FreqDist(bigramas_filtrados)
frecuencias_bigramas_filtrados.plot(10)

# podemos generalizar esto para n-gramas con ngrams()
from nltk.util import ngrams
trigramas = list(ngrams(text1, 3))
frecuencia_trigramas = FreqDist(trigramas)
frecuencia_trigramas.plot(10)

# podemos pasar estos arreglos a dataframes
df = pd.DataFrame()
df['bigramas_filtrados'] = list(set(bigramas_filtrados))
df['palabra_1'] = df['bigramas_filtrados'].apply(lambda x: x[0])
df['palabra_2'] = df['bigramas_filtrados'].apply(lambda x: x[1])
print(df)

### aqui el profe puso una formula y la calculo con los datos del df, procedo a hacer la parte rápida
# las colocaciones son conjuntos de palabras que tienen una inusual alta frecuencia, es decir, son favorecidas más o menos por tradición más que por si significado
from nltk.collocations import * # importamos un paquete pa encontrar colocaciones
bigram_measure = nltk.collocations.BigramAssocMeasures()
finder = BigramCollocationFinder.from_words(text1)
finder.apply_freq_filter(20) # que los bigramas tengan una frecuencia mayor a 20
mayores = finder.nbest(bigram_measure.pmi, 10) # muestra los 10 con mayor pmi (pointwase mutual information)
print(mayores)