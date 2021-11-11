#  Este algoritmo toma los dos elementos adyacentes, vee cual es mayor, y el mayor lo deja a la izquierda y
#  el menor a la derecha.
#  lo anterior es realizando el ordenamiento de forma ascentente

import random as random

# creo mi lista con una cantidad "cantidadNumeros" de numeros, los numeros estarán entre a y b
cantidadNumeros = 100
a, b = 0, 10
randomlist = [random.randint(a, b) for i in range(cantidadNumeros)]
print(randomlist)

# ahora realizaré el sorting
swap = True  # swap en ingles es intercambio
while swap == True:
    swap = False  # asumo que no van a haber cambios
    for i in range(len(randomlist)-1):
        if randomlist[i] > randomlist[i+1]:
            swap = True  # dado que hay intercambios voy a mantener el ciclo
            randomlist[i], randomlist[i + 1] = randomlist[i+1], randomlist[i]
            # tambien pude haber usado un intermediario
            # intermediario = randomlist[i]
            # randomlist[i] = randomlist[i+1]
            # randomlist[i+1] = intermediario
print()
print(randomlist)
