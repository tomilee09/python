# sabemos lo que son las iteraciones
print("iteracion del ciclo for")
for _ in range(1, 4):
    print(_)
print()
# pero lo anterior es azucar sintáctica, en realidad no funcionan así
# las iteraciones, primero entendamos que son los iteradores
# los iteradores son elementos iterables. Ej:
lista = [1, 2, 3]
tupla = (1, 2, 3)
cadena_de_texto = "123"

# podemos transformar estos elementos en iteradores con iter()
iterador_lista = iter(lista)
iterador_tupla = iter(tupla)
iterador_cadena_de_texto = iter(cadena_de_texto)

# y podemos iterar los iteradores con next()
print("iteracion de la lista")
print(next(iterador_lista))
print(next(iterador_lista))
print(next(iterador_lista), "\n")

print("iteracion de la tupla")
print(next(iterador_tupla))
print(next(iterador_tupla))
print(next(iterador_tupla), "\n")

print("iteracion de la cadena de texto")
print(next(iterador_cadena_de_texto))
print(next(iterador_cadena_de_texto))
print(next(iterador_cadena_de_texto), "\n")

# si no sabemos el largo de la lista (y no podemos usar cosas como len())
# entonces podemos usar try y except
nuevo_iterador = iter(lista)
print("iteracion con try-except")
while True:
    try:
        element = next(nuevo_iterador)
        # aqui iría el código de lo que queremos hacer con este elemento
        print(element**2)
    except StopIteration:
        break
# El ciclo for es azucar sintáctico para hacer lo anterior, esa es la 
# forma real en que python realiza las iteraciones



# Al igual que con las listComprehencions y las DictComprehencions puedo
# hacer las iterador-Comprehensions. Ej:
lista = [i**2 for i in range(6)]
print(lista)

iterador = (i**2 for i in range(6))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))

# ejemplo de uso
suma_gen = sum(i for i in range(100))
print(suma_gen)