import pandas as pd
import numpy as np

# creamos una serie (DataFrame en 1D)
series = pd.Series([1, 2, 3, 4, 5])
print(series)

# podemos ver el tipo
print(type(series))

# ver un elemento en específico
print(series[3])

# creamos un DataFrame
df = pd.DataFrame([1, 2, 3])
print(df)

# crear un df a partir de un array
df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6]]))
print(df)

# crear un df a partir de un diccionario
dict = {
    "year": [1, 2, 3],
    "nacimientos": [10032, 32586, 89326],
}
df = pd.DataFrame(dict)
print(df)

# importar un archivo csv
dfSongs = pd.read_csv("canciones_2018.csv")
print(dfSongs.head(5))

# imprimir una columna 
print(dfSongs.artists)

# imprimir una fila
print(dfSongs.iloc[5])

# ver el tamaño del archivo
print(dfSongs.shape)

# ver todas las columnas
print(dfSongs.columns)

# ver muchos datos de una columna
print(dfSongs['tempo'].describe())

# tomar un subset
subset = dfSongs[['name', 'tempo', 'duration_ms']]
print(subset)

# ordenar por columna
subset_ordenado = subset.sort_values(by='tempo', axis=0, ascending=True)
print(subset_ordenado)