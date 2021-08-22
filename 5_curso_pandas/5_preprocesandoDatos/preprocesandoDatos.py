import pandas as pd 

####importamos primero los datos que necesitamos####

df_meteorites = pd.read_csv('/mnt/c/Users/tomilee/Desktop/programacion/python/5_curso_pandas/4_meteoritos/Meteorite_Landings.csv')

#mejoramos los tipos de los datos

df_meteorites = df_meteorites.convert_dtypes()

#podemos ver cuantos datos diferentes hay en nuestra tabla

print(df_meteorites.nunique())

#notamos que hay 2 variables que solo tienen 2 posibles valores

print(df_meteorites[['fall', 'nametype']])

#vemos que son solo texto, asi que lo vamos a cambiar hacia una variable categorica

df_meteorites[['fall', 'nametype']] = df_meteorites[['fall', 'nametype']].astype('category')

#notamos que al imprimirlo ahora las 2 columnas son el tipo category

print(df_meteorites.dtypes)

#podemos ahorrar espacio transformando la variable fall y la variable nametype en variables dummies
#la variable fall tiene solo 2 posibles estados, fell y found,
#con esto se guardaran como 0's y 1's
#se puede hacer lo mismo para nametype

df_meteorites[['fell', 'found']] = pd.get_dummies(df_meteorites['fall'])

#puedo crear una columna facilmente

df_meteorites['ones'] = 1 
print(df_meteorites)

#podemos transformar un texto en una variable de tipo tiempo

df_meteorites['year'] = pd.to_datetime(
    df_meteorites['year'],
    errors = 'coerce', #si un archivo no tiene formato tiempo se crea una varible no numerica
    format = '%m/%d/%Y %H:%M:%S %p'
)
print(df_meteorites.dtypes)

#dato extra, con el tiempo listo podemos usar como variables las horas, dias, etc...
df_meteorites['hour'] = df_meteorites['year'].dt.hour
print(df_meteorites)

# si quiero cambiar el nombre de alguna columna
#df_meteorites = df_meteorites.rename(columns={'mass (g)': 'mass'})
# y si quiero que se guarden los cambios altiro en vez de hacer la igualdad

df_meteorites.rename(columns={'mass (g)':'mass'}, inplace=True)
print(df_meteorites.dtypes)

#podemos ver facilmente los nombres de las columnas

print(list(df_meteorites))
#o con 
print(df_meteorites.columns)

#podemos seleccionar los numeros por multiplos (pares, impares, de tres en tres, etc...)
print(df_meteorites.iloc[::2])

####guardo los datos para usarlo en el siguiente script####
df_meteorites.to_csv('meteo_mejorado.csv')