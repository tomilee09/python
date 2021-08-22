import pandas as pd

####importamos primero los datos que necesitamos####
df = pd.read_csv('london_merged.csv')

print(df.dtypes)

#podemos borrar timestamp y asi tener solo datos numericos
df.drop(['timestamp'], axis=1, inplace=True)
print(df.dtypes)

#ahora con solo datos numericos podemos, por ejemplo, elevar todo al cuadrado
print(df.head(3))
print((df**2).head(3))

#podemos aplicar una operacion solo a una columna
print(df['wind_speed']**2)

#y podemos hacer cosas matelocas
import numpy as np
print(np.sin(df['wind_speed']**2)+100)

#podemos hacer operaciones entre columnas
print((df['wind_speed']-df['hum']).head(3))
print((df['wind_speed']+df['hum']).head(3))
print((df['wind_speed']*df['hum']).head(3))
print((df['wind_speed']/df['hum']).head(3))
print((df['wind_speed']**df['hum']).head(3))

#si nos faltan datos para hacer la operacion entre columnas entonces se completaran espacios vacios con un no numerico
print(df['wind_speed'].iloc[::2]-df['hum'])

#si queremos que ese no sea un no numerico podemos darle un valor a la fila para cuando no tenga un dato con fill_value
print(df['wind_speed'].iloc[::2].sub(df['hum'], fill_value = 1000))
#todas las operaciones basicas tienen eso: add(), sub(), mul(), div(), mod(), pow()

#tambien hay producto punto (multiplicacion de columnas y sumar todo)
print(df['wind_speed'].dot(df['hum']))

#podemos crear funciones y aplicarlas a las columnas
def funcion(x):
    x=x**2+3*x
    return x
print(df['wind_speed'].apply(funcion))

#podemos ponerle argumentos a la funcion y aplicarla
def funcion_2(x, a=1, b=3):
    x=x**2+3*x + a + b
    return x
print(df['wind_speed'].apply(funcion_2, a=3, b=4))

#podemos poner una funcion lambda
print(df['wind_speed'].apply(lambda x: x+2000))

#una aplicacion es aplicarle el promedio a todas las columnas
print(df.apply(lambda x: x.mean()))

#o el promedio de todas las filas
print(df.apply(lambda x: x.mean(), axis=1))

#tambien aplicar la desviacion estandar
print(df.apply(lambda x: x.std()))

#pero si quiero hacer un cambio para todos los datos individuales debo ocupar applymap
print(df.applymap(lambda x: x+1000))

#podemos cambiar el valor de una columna con map
print(df['wind_speed'].map('la velocidad del viento es: {}'.format))