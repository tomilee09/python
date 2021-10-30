# otras estructuras de datos son las singly (o double) linked list
# tal como dice su nombre son listas unidas por un solo camino (o 2 en el caso de las double), se deja una imagen que lo explica bastante bien
# estos solo pueden tomar elementos que están directamente delante o directamente detrás
# Ejemplos de uso: historial de navegación, Ctrl + z, gif (aunque claramente podrían ser usadas listas, depende del caso de uso ver si es mejor usar las SLL o DLL)
# los valores de las SLL y DLL están unidas mediante nodos (tienen valor y referencia)
# Los SLL y DLL son simplemente formas de ordenar los nodos
# crearemos aqui los SLL mediante la clase de nodos


import sys 
sys.path.append("../nodos/")
from nodos import Nodo

class SinglyLinkedList:
    def __init__(self):
        self.tail = None
        self.size = 0 # la usaremos pa gaurdar el tamaño del SLL, dado que no tenemos métodos como len()
    
    def añadir_nodos(self, valor):
        nodo_por_agregar = Nodo(valor)

        # vamos a avanzar en la lista hasta llegar al último valor del SLL, y a ese le daremos el valor del nodo por agregar
        # si no tenemos nodos
        if self.tail == None:
            self.tail = nodo_por_agregar
        else: 
            nodo_donde_estamo = self.tail
            # avanzamos a travez de los nodos
            while nodo_donde_estamo.referencia: # mientras vayamos avanzando
                nodo_donde_estamo = nodo_donde_estamo.referencia # avanza hacia donde apuntas
            nodo_donde_estamo.referencia = nodo_por_agregar # el último nodo que tengamos debe puntar hacia el nodo que queremos agregar
        self.size += 1 
    
    def tamano(self):
        return self.size

    def iterar(self):
        nodo_donde_estamo = self.tail