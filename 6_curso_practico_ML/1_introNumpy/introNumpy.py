import numpy as np

A = np.array([1, 2, 3, 4, 5, 6, 7])

# mostrar una lista
print(A[1])
print(A[1:7])
print(A[1::2])

# crear listas y matrices
print(np.zeros(10))
print(np.ones((3, 3)))

# ver el tipo
print(type(np.zeros(10)))
print(type(np.ones((3, 3))))

# crear arreglos rapido
print(np.linspace(0, 8, 5))

# ordenar algo rapido
a = np.array([10, 7, 111, 1, 5, 2])
print(np.sort(a))

# crear rangos unidimensionales
print(np.arange(1, 10, 3))

# crear matrices con un valor
print(np.full((4, 4), 10))
print(np.diag([1, 2, 3]))