import pandas as pd

####importamos primero los datos que necesitamos####
df_meteorites = pd.read_csv('/mnt/c/Users/tomilee/Desktop/programacion/python/5_curso_pandas/5_preprocesandoDatos/meteo_mejorado.csv')

#borramos la columna con puros 1's
df_meteorites.drop(['ones'], axis=1, inplace=True)
print(df_meteorites.head(3), '\n')

#podemos borrar filas por su indice
df_meteorites.drop([0, 1, 2], axis=0, inplace=True)
print(df_meteorites.head(3), '\n')

#podemos borrar filas y columnas al mismo tiempo
df_meteorites.drop(columns=['id', 'reclat'], index=[3, 4, 5], inplace=True)
print(df_meteorites.head(3), '\n')

#tambien podemos borrar con la herramienta de busqueda
#aqui borre la primera columna
df_meteorites = df_meteorites.iloc[:,1:]

#podemos hacer una copia y ahi hacer los cambios pa no mandarnos una embarrada
#la copia debe ser profunda pues sino los cambios de la copia se harán en el original
df = df_meteorites.copy(deep=True)
df.drop(columns=['name', 'nametype'], index=[6, 7, 8], inplace=True)
print(df_meteorites.head(3), '\n')
print(df.head(3), '\n')