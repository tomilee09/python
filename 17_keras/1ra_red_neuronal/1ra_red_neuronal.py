import numpy as np
from keras import layers, models
from keras.utils import to_categorical
from keras.datasets import mnist
import matplotlib.pyplot as plt

# para este caso, data son fotos y labels son etiquetas (los números que aparecen en las fotos)
(train_data, train_labels), (test_data, test_labels) = mnist.load_data() 
n = 55
print(train_data.shape)
plt.imshow(train_data[n])
print(train_labels[n])
plt.show()

# ahora vamos a crear el modelo
modelo = models.Sequential() # declaramos el modelo
modelo.add(layers.Dense(512, activation = "relu", input_shape = (28*28,))) # creamos la capa donde se procesa la info
modelo.add(layers.Dense(10, activation = "softmax")) # creamos la capa final donde se entrega el resultado
modelo.compile(optimizer = "rmsprop", 
                loss = "categorical_crossentropy", 
                metrics = "accuracy") # vemos la forma en que se compilará la red neuronal
print(modelo.summary()) # pedimos un resumen del modelo creado