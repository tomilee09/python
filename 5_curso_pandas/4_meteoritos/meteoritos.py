import pandas as pd 

df_meteorites = pd.read_csv('Meteorite_Landings.csv')

print(df_meteorites)

#dado que son muchos datos podemos elegir que datos imprimir
#podemos imprimir los primeros datos
print(df_meteorites.head(10))

#podemos imprimir los ultimos datos
print(df_meteorites.tail(10))

#podemos imprimir aleatoriamente datos
print(df_meteorites.sample(10))

#podemos ver el numero de filas y columnas
print(df_meteorites.shape)

#podemos ver el total de datos (numero_filas*numero_columnas)
print(df_meteorites.size)

#podemos obtener muchos datos de una
print(df_meteorites.describe())

#podemos modificar la forma en la que se muestran los datos
pd.options.display.float_format = '{:,.1f}'.format
print(df_meteorites.describe())

#podemos obtener aun mas datos
print(df_meteorites.describe(include = 'all'))

#podemos saber los tipos de los datos segun las categorias
print(df_meteorites.dtypes)

#podemos cambiar los tipos para que se optimise el funcionamiento de los datos
df_mejorado = df_meteorites.convert_dtypes()
print(df_mejorado.dtypes)

####Extra####
#import seaborn as sns
#sns.boxplot(df['mass (g)'])