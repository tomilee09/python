import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# importamos los datos que utilizaremos 
salarios = pd.read_csv('salarios.csv')

# vemos cuantos datos tenemos
print(salarios.shape)

# definimos los valores de las x e y
x = salarios["Aexperiencia"].values.reshape(30,1)
y = salarios["Salario"].values.reshape(30,1)

# ahora seleccionamos los datos para entrenamiento y para testear si funciono
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 1)

# con lo anterior ya podemos hacer la regresion lineal
ajusteLineal = LinearRegression().fit(x_train, y_train)

# ploteamos
plt.scatter(x_train, y_train, color = "black")
plt.plot(x_train, ajusteLineal.predict(x_train), color = "blue")
plt.show()

# comprobacion de que tan buena fue la aproximacion, mostramos los puntos de prueba (test) junto con el ajuste de los puntos de entrenamiento
plt.scatter(x_test, y_test, color = "black")
plt.plot(x_train, ajusteLineal.predict(x_train), color = "blue")
plt.show()

# tambien podemos pedirle a scikit learn que vea que tan buena fue la aproximacion con .score
print(ajusteLineal.score(x_test, y_test))
# esto nos dice que un 87% de los datos estan cerca de la recta (o eso entendi de la clase)