import sympy as sp 

# podemos resolver esto de la forma Ax = b, con A una matriz y b un vector
A = sp.Matrix([[1, 2], [3, 4]])
b = sp.Matrix([1, 2])
soluciones = A.solve(b)
print(soluciones)

# esto tambien lo podemos hacer con scipy y numpy (aproach numerico)
import scipy.linalg as la  
import numpy as np
A = np.array([[1, 2], [3, 4]])
b = np.array([1, 2])
solucion_scipy_numpy = la.solve(A, b)
print(solucion_scipy_numpy)

# tambien podemos resolver sistemas rectangulares (más variables que ecuaciones) con sympy
variables = sp.symbols("x, y, z")
A = sp.Matrix([[1, 2, 3], [4, 5, 6]])
x = sp.Matrix(variables)
b = sp.Matrix([1, 2])
solucion_rectangular = sp.solve(A*x-b, variables)
print(solucion_rectangular)