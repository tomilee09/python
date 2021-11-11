from nodos import Nodo

nodo1 = Nodo("valor nodo 1", None)
nodo2 = Nodo("este es un valor del nodo 2", nodo1)
nodo3 = Nodo("hola nodo 1 :)", nodo2)
print(nodo1.valor)
print(nodo2.referencia.valor)  # obtuve el valor del nodo 1 a partir del nodo 2
print(nodo3.referencia.valor)  # valor del nodo 2 a partir del nodo 3

# lo anterior es un conjunto de datos con direcciones, es como un grafo
# las direcciones van así:
# nodo1 <- nodo2 <- nodo3
# aunque no es necesario que las direcciones sean secuenciales


############# creo un singly linked list ##############
def transformSll(lista_elementos):
    """Esta es una función que crea una single linked list a partir de una lista común de python"""
    # invierto la lista porque así puedo ir creando las referencias de forma ascendiente en la lista
    # (para que el 1 apunte al 2, el 2 tiene que estar ya creado, por eso el orden de agregacion debe ser 5, 4, 3, 2, 1)
    lista_elementos.reverse()
    i = -1  # parto del -1 para tener en cuenta el primer caso además necesito saber el valor de i para hacer las referencias
    sll = []
    # voy agregando los nodos a la lista en el ciclo for
    for valor in lista_elementos:
        if i == -1:
            sll.append(Nodo(valor, None))
        # elif i == len(lista_elementos):
        #     sll.append(Nodo(valor, None))
        else:
            sll.append(Nodo(valor, sll[i]))
        i += 1
    sll.reverse()
    return sll


# a partir de una lista creo un sll con mi funcion
lista = [1, 2, 3, 4, 5]
sll = transformSll(lista)

# imprimo los valores y referencias de los nodos de la lista
print()
for i in range(len(lista)):
    print(f'valor {i} es: {sll[i].valor}')
    print(f'su referencia es {sll[i].referencia.valor}') if i != 4 else print(
        "este no tiene referencia")

# a pesar de que esto parece mucho un sll, no lo es, es una lista de nodos, falta crear métodos para avanzar entre los nodos o retroceder y asi...
