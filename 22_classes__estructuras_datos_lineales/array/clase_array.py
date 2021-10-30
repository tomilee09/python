# los arrays son un subtipo de lista (haciendo referencia a la clase "lista" ya incorporada en python)
# es como una lista pero con restricciones, en los arrays no se puede:
# agregar posiciones
# remover posiciones
# modificar tamaño del array mismo (se define al momento de crearlo, si se crea con 5 elementos ese es su máximo y mínimo de elementos)

# recordar que las clases por convención van con mayúsculas y que usan CamelCase
class Array:
    def __init__(self, capacidad, valor_inicial = 0):
        self.items = [valor_inicial for i in range(capacidad)]

    def largo(self):
        return len(self.items)
    
    def imprimir(self):
        return str(self.items) # str es una función ya creada por python

    def iterador(self):
        return iter(self.items) # lo creo porque podría llegar a ser más fácil recorrer los elementos

    def tomarElemento(self, indice):
        return self.items[indice]

    def cambiarValor(self, indice, valor):
        self.items[indice] = valor


### DE AQUI EN ADELANTE ES UN RETO, NO ES PARTE DE LAS FUNCIONES DE UN ARRAY ###


    def nosVolvimoLocos(self):
        import random
        self.items = [random.randint(0, 10) for i in self.items]
    
    def sum(self):
        suma = 0
        for i in range(len(self.items)):
            suma += self.items[i]
        return suma