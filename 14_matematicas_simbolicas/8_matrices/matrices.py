import sympy as sp   

# podemos trabajar simbolicamente con matrices
print(sp.Matrix([[1, 2], [3, 4]]))

# creemos una matriz con letras y trabajemos con ella
a, b, c, d = sp.symbols("a, b, c, d")
m = sp.Matrix([[a, b], [c, d]])



print(m)
print(m+m)
print(m*m)
print(m**2)
print(m.det()) # determinante
print(m.T) # transpuesta
print(m.trace()) # traza
print(m.inv()) # inversa
print(m.H) # adjunta 
print(m.diagonalize()) # diagonalizacion 
print(m.norm()) #norma 
