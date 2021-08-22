from sklearn.cluster import KMeans
from sklearn import datasets
from sklearn import metrics
import pandas as pd
import matplotlib.pyplot as plt

iris = datasets.load_iris()

X_iris = iris.data
Y_iris = iris.target

x = pd.DataFrame(X_iris, columns = ['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width'])
y = pd.DataFrame(Y_iris, columns =['Target'])

plt.scatter(x['Petal Length'], x['Petal Width'])
plt.show()

#### aqui comienza la parte de machine learning ####

model = KMeans(n_clusters= 3, max_iter= 10)
model.fit(x)
y_labels = model.labels_
y_kmeans = model.predict(x)
print(y_kmeans)

presicion = metrics.adjusted_rand_score(Y_iris, y_kmeans)
print(presicion)

# graficamos pero ahora con las subdiviciones
plt.scatter(x['Petal Length'], x['Petal Width'], c = y_kmeans)
plt.show()