import pandas as pd 
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import seaborn as sns

diabetes = pd.read_csv('diabetes.csv')

# cuantos pacientes tenemos?
print(diabetes.shape)

# veamos todos los datos que se tienen de los pacientes
print(diabetes.columns)

# indicamos las caracteristicas necesarias para nuestro estudio
colsConsideradas = ['Glucose', 'Insulin', 'Age', 'BloodPressure', 'DiabetesPedigreeFunction']
x = diabetes[colsConsideradas]
y = diabetes.Outcome # es una de las columnas e indica si tiene diabetes (1) o no (0)

# Ahora definimos los datos de entrenamiento y testeo con scikit learn
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state = 0)

# con los datos de entrenamiento realizamos la regresion logistica
reglog = LogisticRegression().fit(X_train, y_train)

# mostramos los pacientes con diabetes (1) y sin diabetes (0) del grupo de testeo
print(reglog.predict(X_test))

# ahora comprobamos que tal fue la predicción con la matriz de confision, que indica [[positivos, falsos negativos], [falsos positivos, negativos]]
confusionMatrix = metrics.confusion_matrix(y_test, reglog.predict(X_test))
print(confusionMatrix)

# podemos tambien ver la probabilidad de que el programa acierte, o sea su exactitud, que es "(verdaderos positivos + verdaderos negativos)/total de datos"
print(metrics.accuracy_score(y_test, reglog.predict(X_test)))