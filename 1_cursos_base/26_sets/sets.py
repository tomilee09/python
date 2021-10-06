# Los sets son como las listas, pero no pueden tener elementos repetidos
# además guardan sus elementos de forma desordenada 
# por último, los elementos de los sets deben ser inmutables 
# Los sets se crean a partir de corchetes (como los diccionarios, pero a
# los sets no hay que ponerle los dos_puntos (:)). Ej:

miLista = ["hola", 1, 2, 4, 3, "hola", 5, 1, 2, 3, 4]
miSet = {"hola", 1, 2, 4, 3, "hola", 5, 1, 2, 3, 4}
print(miLista)
print(miSet) # borra elementos duplicados y les cambia el orden

# NOTA: por esto en internet pa borrar elementos duplicados de una lista
# daban el consejo de poner el siguiente código: 
# miLista = list(set(miLista))
# al transformarlo en set se borran los duplicados y despues lo devolvian
# a el tipo lista

# si pongo solo corchetes python cree ue es un diccionario
diccionario = {}
print(type(diccionario))

# para crear un set vacio se debe poner la palabra clave set()
set_vacio = set()
print(type(set_vacio))

# para añadir elementos a los sets se le debe poner add() (para elementos únicos) o update() (para listas, sets o tuplas)
nuevoSet = {1, 2, 3}
nuevoSet.add(4) # puedo poner solo un elemento a la vez aqui
nuevoSet.update([1, 10, 9], {238, 1209}, (0, -10))
print(nuevoSet)

# para eliminar elementos de los sets puedo usar discard() o remove() (la diferencia es que remove tira un error si no está el elemento)
nuevoSet.discard(2)
nuevoSet.remove(1)
nuevoSet.discard(20) # esto no da error a pesar de que 20 no exista en el set
#nuevoSet.remove(30) # esto da error porque el 30 no existe en el set

# además se puede usar .pop() y .clear()
nuevoSet.pop() # borra un elemento aleatorio del set
nuevoSet.clear() # borra todos los elementos del set
print(nuevoSet)

# OPERACIONES ENTRE SETS
# las siguientes son las tipicas operaciones entre conjuntos
set1 = {1, 2, 3}
set2 = {2, 3, 4}
# union -> guarda los elementos que contenga el set1 o (signo |) el set2
union = set1 | set2
print(f'la union de mis sets {set1} y {set2} es: {union}')

# intersección -> guarda los elementos que contenga el set1 y (signo &) el set2
interseccion = set1 & set2
print(f'la intersección de mis sets {set1} y {set2} es: {interseccion}')

# diferencia -> guarda los elementos que contenga el set1 que no contenga el set2
diferencia = set1 - set2
print(f'la diferencia de mis sets {set1} y {set2} es: {diferencia}')

# diferencia simétrica -> guarda los elementos que no compartan el set1 con el set2 (es lo contrario a la intersección)
diferencia_simetrica = set1 ^ set2
print(f'la diferencia simétrica de mis sets {set1} y {set2} es: {diferencia_simetrica}')
