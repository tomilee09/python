# forma malandra, otaku, sucia
miDiccionario = {}
for i in range(11):
    if i%3==0:
        miDiccionario[i] = i**2
print(miDiccionario)

# forma pro carita_fachera_facherita
diccionarioPro = {i:i**2 for i in range(11) if i%3==0}
print(diccionarioPro)

# podemos ponerle aun más facha creando el diccionario a partir de 2 listas
numeros = [i for i in range(1, 4)]
nombresAlumnos = ["Tomás", "Lorena", "Andrea"]
ListaAlumnos = {numero:nombre for numero, nombre in zip(numeros, nombresAlumnos)}
print(ListaAlumnos)

# NOTA: LO QUE HACE ZIP() ES LO SIGUIENTE
# >>> x = [1, 2, 3]
# >>> y = [4, 5, 6]
# >>> zipped = zip(x, y)
# >>> list(zipped)
# [(1, 4), (2, 5), (3, 6)]