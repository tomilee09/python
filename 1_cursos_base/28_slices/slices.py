# Los slices (traducido como rodajas o debanadas) son formas en las que podemos tomar los elementos de un iterable
palabra = "electroencefalograma"
#palabra = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # funciona con listas
#palabra = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) # funciona con tuplas
#palabra = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} # no funciona con sets
#palabra = {i:i**2 for i in range(20)} no funciona con diccionarios

print(palabra[:]) # entrega la palabra completa
print(palabra[1:3]) # toma los indices 1 y 2 pero el 3 no porque no es inclusivo
print(palabra[:4]) # toma todos hasta el cuerto (no inclusivo)
print(palabra[4:]) # toma todos desde el cuarto (inclusivo)
print(palabra[-4:]) # toma los ultimos 4 elementos (se lee como desde los ultimos 4 elementos hasta el final)
print(palabra[0:-1]) # toma desde el primer elemento hasta el penúltimo
print(palabra[0:10:2]) # toma desde el primero hasta el noveno de 2 en 2 
print(palabra[::]) # entrega la palabra completa (equivalente a palabra[0:len(palabra):1])
print(palabra[::-1]) # entrega la palabra pero de -1 en -1, es decir, va hacia atras de uno en uno, es decir, entrega la palabra invertida 

