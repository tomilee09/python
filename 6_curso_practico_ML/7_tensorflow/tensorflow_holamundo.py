import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

fashion_mnist = keras.datasets.fashion_mnist
(train_images , train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

#plotear imagenes
#plt.figure()
#plt.imshow(train_images[100])
#plt.grid(True)
#plt.show()

#normalizamos los valores de los pixeles de las imagenes (que no vayan de 0 a 255 sino que de 0 a 1)
train_images = train_images / 255.0
test_images = test_images /255.0

# ploteamos varias imagenenes para ver el dataset
#plt.figure(figsize = (10,10)) # imagenes se mostraran en tamaños de 10x10 pixels
#for i in range(25):
#    plt.subplot(5, 5, i+1)
#    plt.imshow(train_images[i], cmap = plt.cm.binary) #binary lo plotea en blanco y negro
#    plt.xlabel(class_names[train_labels[i]])
#plt.show()

# ahora creamos el modelo

model = keras.Sequential([keras.layers.Flatten(input_shape = (28,28)), keras.layers.Dense(128, activation = tf.nn.relu), keras.layers.Dense(10, activation = tf.nn.softmax)])