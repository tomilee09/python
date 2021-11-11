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
    """clase de sll, creada sin listas (cree un sll con listas en el main.py de nodos.py), solo nodos que se unen con otros por referencia """

    def __init__(self):
        self.tail = None  # partimos sin elementos
        self.size = 0  # la usaremos pa gaurdar el tamaño del SLL, dado que no tenemos métodos como len()
        # esta variable auxiliar servirá para movernos dentro de la sll (la uso en avanzar)
        self.posicion = self.tail
        self.contador = 0  # lo voy a usar pa saber la posicion en la que voy

    def add(self, valor):
        nodo_por_agregar = Nodo(valor)

        # dado que no usamos listas no podemos simplemente agregar un valor mediante indice a la lista
        # vamos a avanzar en la lista hasta llegar al último valor del SLL, y a ese le daremos el valor del nodo por agregar
        if self.tail == None:  # si no tenemos nodos
            self.tail = nodo_por_agregar  # vamos a poner el nodo por agregar como el primer nodo
        else:
            # si ya tenemos nodos vamos a crear la variable nodo_donde_estamo para llegar hasta el último nodo y ahí guardar el nuevo nodo nodo_por_agregar
            nodo_donde_estamo = self.tail  # partimos desde el primer nodo
            # avanzamos a travez de los nodos
            # mientras el nodo donde estamos tenga una referencia (un nodo al cual está apuntando)
            while nodo_donde_estamo.referencia:
                nodo_donde_estamo = nodo_donde_estamo.referencia  # avanza hacia donde apunta
            # al terminar el ciclo anterior llegamos al último nodo en nuestro sll, a este nodo le decimos que su referencia será el nodo que queremos agregar (agregando así el nodo)
            nodo_donde_estamo.referencia = nodo_por_agregar
        self.size += 1

    def addList(self, lista):
        # si ya tenemos nodos vamos a crear la variable nodo_donde_estamo para llegar hasta el último nodo y ahí guardar el nuevo nodo nodo_por_agregar
        nodo_donde_estamo = self.tail  # partimos desde el primer nodo
        # avanzamos a travez de los nodos
        # mientras el nodo donde estamos tenga una referencia (un nodo al cual está apuntando)
        while nodo_donde_estamo.referencia:
            nodo_donde_estamo = nodo_donde_estamo.referencia  # avanza hacia donde apunta

        # voy agregando los nodos a la lista en el ciclo for
        for valor in lista:
            # transformo el valor en un nodo que no apunta a nada (si agrego otro elemento le indico donde apuntar)
            nodo_por_agregar = Nodo(valor)
            # hago que el ultimo nodo de la sll apunte a el nodo por agregar
            nodo_donde_estamo.referencia = nodo_por_agregar
            # me muevo al último nodo agregado pa seguir agregando
            nodo_donde_estamo = nodo_donde_estamo.referencia
            self.size += 1

    def tamano(self):
        """entrega el tamaño del sll"""
        return self.size

    def iterar(self):
        """itera el sll, es decir, pasa por todos los elementos"""
        nodo_donde_estamo = self.tail

    def print(self):
        """muestra en pantalla todo el sll"""
        # si la sll está vacia entonces mostramos un mensaje
        if self.tail == None:
            print("Linked list is empty")

        # si no está vacía mostramos los elementos
        else:
            i = self.tail
            texto = ''
            while i:  # mientras exista un valor
                texto += str(i.valor)
                if i.referencia:  # si existe referencia entonces muestra una flechita
                    texto += '-->'
                i = i.referencia

            print(texto)

    def showPosicion(self):
        """muestra en terminal el valor de la posicion en la que se encuentra"""
        if self.contador == 0:
            self.posicion = self.tail
        print(self.posicion.valor)

    def next(self):
        """avanza dentro de la sll (cambiando la posicion)"""
        if self.contador == 0:
            self.posicion = self.tail.referencia
        else:
            self.posicion = self.posicion.referencia
        self.contador += 1

    def resetPosicion(self):
        """hace que se vuelva a la posicion original"""
        self.contador = 0

    def sll2circular(self):
        # hago lo mismo que para añadir un elemento, avanzo hasta el último elemento
        nodo_donde_estamo = self.tail
        while nodo_donde_estamo.referencia:
            nodo_donde_estamo = nodo_donde_estamo.referencia
        # hago que el último nodo apunte al primero, haciendo un circular linked list
        nodo_donde_estamo.referencia = self.tail

    def circular2sll(self):
        # dado que ahora con la circular linked list tengo "infinitos" elementos tengo que usar un ciclo for junto con la variable size para avanzar
        nodo_donde_estamo = self.tail
        for i in range(self.size-1):
            nodo_donde_estamo = nodo_donde_estamo.referencia
        # hago que el último nodo no apunte a otro nodo, haciendo un single linked list
        nodo_donde_estamo.referencia = None

    def insert(self, valor):
        """insertará un elemento entre la posicion en la cual se encuentre self.posicion y self.posicion.referencia"""
        nuevoNodo = Nodo(valor, self.posicion.referencia)
        self.posicion.referencia = nuevoNodo

    def erase(self):
        """borrará el elemento en el cual se encuentre la posicion (en realidad simplemente voy a hacer que este nodo sea igual al siguiente, así ambos apuntarán al subsiguiente y parecerá como si solo hubiera uno, de hecho es probable que python elimine alguno en el procesamiento con su garbage collector)"""
        self.posicion.valor = self.posicion.referencia.valor
        self.posicion.referencia = self.posicion.referencia.referencia
