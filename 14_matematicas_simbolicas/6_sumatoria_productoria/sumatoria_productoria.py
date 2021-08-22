import sympy as sp    

# para hacer la sumatoria creamos un entero n
n = sp.Symbol('n', integer = True)
suma = sp.Sum(1/(n**2), (n, 1, sp.oo))
print(suma.doit())

# podemos tambien hacer el factorial, haciendo la productoria de los numeros de 1 a n (en este caso tomo n = 7 como cota superior)
factorial = sp.Product(n, (n, 1, 7))
print(factorial.doit())
