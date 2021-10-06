# Funcion de orden superior es una funcion que acepta como input otra funcion
# Ej:
high_order = lambda a: a() # ejecuta la funcion que tiene como input
hola = lambda : print("hola")
chao = lambda : print("chao")
high_order(hola)
high_order(chao)

# de estos las funciones importantes que son HOF son: filter, map, reduce
# Ej: obtener solo pares || ejemplo con filter
numeros = [i for i in range(11)]
# esto podemos resolverlo con list comprehensions
pares = [i for i in numeros if i%2==0]
print(pares)
# intentemos ahora con filter
pares_filter = list(filter(lambda i:i%2==0, numeros))
print(pares_filter)
# lo que hizo filter fue ir viendo por cada elemto a ver si se cumplia 
# la condicion que le pusimos en la funcion lambda, si se cumple el
# numero se guarda en la lista pares_filter

# Ej: elevar al cuadrado || ejemplo con map
numeros = [i for i in range(6)]
# esto podemos resolverlo con list comprehensions
cuadrado = [i**2 for i in numeros]
print(cuadrado)
# intentemos ahora con filter
cuadrado_map = list(map(lambda i:i**2, numeros))
print(cuadrado_map)
# lo que hace MMMMMap es ir MMMModificando los numeros segun la funcion
# que le dimos y guarda los valores en cuadrado_map

# Ej: multiplicar elementos de una lista || ejemplo con reduce
numeros = [i for i in range(1, 11)] # pa hacer factorial(10)
# esto podemos resolverlo con ciclos for
factorial = 1
for i in numeros:
    factorial = factorial*i
print(factorial)
# intentemos ahora con reduce
# esta funcion no viene incluida así que hay que importarla
from functools import reduce
factorial_reduce = reduce(lambda a, b:a*b, numeros)
print(factorial_reduce)
# lo que hace reduce es ir cada 2 elementos y realizar la accion que se le
# indica en la funcion lambda, en este caso multiplicacion
# toma los elementos de la siguiente forma
# iteracion 1: a = primer elemento, b = segundo elemento
# iteracion 2: a = resultado anterior, b = tercer elemento
# iteracion 3: a = resultado anterior, b = cuarto elemento
# iteracion 4: a = resultado anterior, b = quinto elemento
# ...