import sympy as sp  
matriz = sp.Matrix([[1, 2], [3, 4]])

# podemos encontrar los eugenvalues facilmente con .eigenvals()
print(matriz.eigenvals())

# podemos encontrar los eigenvectors facilmente con .eigenvects()
print(matriz.eigenvects())



# todo lo anterior lo podemos realizar con numpy y scipy # aproximación numérica
import numpy as np
import scipy.linalg as la

matriz2 = np.array([[1, 2], [3, 4]])
evals, evecs = la.eig(matriz2)

print()
print()
print()

print(evals)
print(evecs)