# el selection sort lo que hace es buscar los menores elementos e ir ordenandolos
# primero toma el elemento más pequeño y lo lleva a la izquierda, después el segundo elemento más pequeño y lo lleva a la izquierda (segunda posicion) y asi...
# además dado este procedimiento sabemos que la cantidad de movimientos a realizar siempre será menor o igual a la cantidad de elementos del array

import random

# creo una lista de cantidadElementos de elementos y con números entre a y b
cantidadElementos = 5
a, b = 0, 10
randomList = [random.randint(a, b) for i in range(cantidadElementos)]
#randomList = [5, 4, 3, 2, 1]
print(randomList)


def selectionSort(listaLoca):
    swap = True
    # iteraciones servirá para ir acortando la lista (no usar los espacios de la izquierda que ya están ordenados)
    iteraciones = 0
    for j in range(len(listaLoca)):
        indice, numero = iteraciones, listaLoca[iteraciones]

        # recorro toda la lista encontrando el menor elemento
        for i in range(iteraciones, len(listaLoca)):
            print(i)
            if numero > listaLoca[i]:
                #print("hola", i)
                indice, numero = i, listaLoca[i]
                swap = True  # dado que encontré un número que ordenar entonces voy a realizar otra iteracion
        # ahora que encontré el número más chico y su índice lo puedo mover
        print(listaLoca[indice])
        listaLoca.insert(iteraciones, listaLoca.pop(indice))
        print(listaLoca)
        iteraciones = iteraciones + 1  # aumento en 1 el valor de iteraciones
        # print(iteraciones)
    return listaLoca


listaOrdenada = selectionSort(randomList)
print()
print(listaOrdenada)
