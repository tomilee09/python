import pandas as pd 

# creemos un diccionario con varias filas 

diccionario = {'tomas':[1, 2, 3], 'lore':[4, 5, 6], 'papa':[7, 8, 9]}
print(diccionario, "\n")

# ahora lo transformamos en un dataframe
dataFrame = pd.DataFrame(diccionario)
print(dataFrame, "\n")

#le podemos cambiar los indices 
dataFrame = pd.DataFrame(diccionario, index = ['nota 1', 'nota 2', 'nota 3'])
print(dataFrame, '\n')

# del dataframe podemos sacar cualquier info
print(dataFrame.index, "\n")
print(dataFrame.columns, "\n")
print(dataFrame.values, "\n")

#podemos saber solo la info de una columna
print(dataFrame['tomas'], '\n')

#podemos sacar varias columnas
print(dataFrame[['tomas', 'lore']],'\n')

#podemos sacar los datos de columnas especificas y filas especificas
#print(dataFrame.loc['filas', 'columnas'])
print(dataFrame.loc['nota 1', 'tomas'], '\n')
print(dataFrame.loc['nota 1', ['tomas', 'lore']], '\n')
print(dataFrame.loc[['nota 1', 'nota 2'], ['tomas', 'lore']], '\n')

#podemos buscar datos a travez de los indices de sus filas y columnas
print(dataFrame.iloc[2, 1], '\n')
print(dataFrame.iloc[[1, 2], [0, 1]], '\n')
print(dataFrame.iloc[:, 1], '\n')

#puedo filtrar con datos que cumplan algun parámetro
print(dataFrame['tomas'] >=2, '\n') #esto estrega un booleano
print(dataFrame[dataFrame['tomas'] >=2], '\n') #este es el weno

#puedo poner mas condiciones
print(dataFrame[(dataFrame['tomas'] >=2) & (dataFrame['lore'] == 5)], '\n') 

#podemos hacer lo mismo con query
print(dataFrame.query('tomas>=2'), '\n')

#tambien puedo filtrar comparando entre columnas
print(dataFrame[dataFrame['lore']>=dataFrame['tomas']], '\n')