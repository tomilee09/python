import pandas as pd

# crear una serie
serie_pandas = pd.Series([15, 16, 17, 18, 19, 20])
print(serie_pandas, "\n")

#mostrar solo valores
valores = serie_pandas.values
print(valores, "\n")

#mostrar la lista de indices (lista de la izquierda de la serie)
indices = serie_pandas.index
print(indices, "\n")

#numero elementos (dimension)
dimension = serie_pandas.shape
print(dimension, "\n")

#llamar elementos
print(serie_pandas[1])
print(serie_pandas[[5, 3, 4, 1]], "\n")

#cambiar los indices
serie_pandas = pd.Series([15, 16, 17, 18, 19, 20], index = ['a', 'b', 'c', 'd', 'e', 'f'])
print(serie_pandas, "\n")

#puedo crear un diccionario y transformarlo a pandas
diccionario = {'tomas': 20, 'lorena': 20, 'martin': 15}
print(diccionario)
diccionario2pandas = pd.Series(diccionario)
print(diccionario2pandas, "\n")