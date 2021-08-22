import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn import tree
from sklearn.model_selection import train_test_split

# importamos los datos con los cuales trabajaremos, los datos de entrenamiento y los datos de testeo
df_train = pd.read_csv('titanic-train.csv')
df_test = pd.read_csv('titanic-test.csv')

# nos informamos de los datos 
print(df_train.columns)
print(df_train.info())

# vamos a depurar los datos 
from sklearn import preprocessing

# vamos a crear los datos train y test




# vamos a eliminar las columnas que no nos sirvan

