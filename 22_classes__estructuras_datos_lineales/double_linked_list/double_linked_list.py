# voy a crear una clase de double linked list (son las sll pero ahora hay 2 referencias, hacia delante y atrás)

from nodos2 import Nodo2


class DoubleLinkedList:
    def __init__(self):
        # los siguientes 2 son pa info general de la dll
        self.tail = None
        self.size = 0
        # los siguientes 2 son pa moverse
        self.posicion = None
        self.contadorPosicion = 0

    def add(self, valor):
        """añade un elemento al dll """
        nodo_por_agregar = Nodo2(valor)

        if self.tail == None:
            self.tail = nodo_por_agregar
        else:
            nodo_donde_estamo = self.tail
            while nodo_donde_estamo.refDelante:
                nodo_donde_estamo = nodo_donde_estamo.refDelante
            nodo_donde_estamo.refDelante = nodo_por_agregar
            nodo_por_agregar.refAtras = nodo_donde_estamo  # esto es lo único que cambia
        self.size += 1

    def print(self):
        """muestra en pantalla todo el dll"""
        # si la sll está vacia entonces mostramos un mensaje
        if self.tail == None:
            print("Linked list is empty")

        # si no está vacía mostramos los elementos
        else:
            i = self.tail
            texto = ''
            while i:  # mientras exista un valor
                texto += str(i.valor)
                if i.refDelante:  # si existe referencia entonces muestra una flechita
                    texto += '<->'
                i = i.refDelante

            print(texto)

    def showPosicion(self):
        """muestra en terminal el valor de la posicion en la que se encuentra"""
        if self.contadorPosicion == 0:
            self.posicion = self.tail
        print(self.posicion.valor)

    def next(self):
        """avanza dentro de la sll (cambiando la posicion)"""
        if self.contadorPosicion == 0:
            self.posicion = self.tail.refDelante
        else:
            self.posicion = self.posicion.refDelante
        self.contadorPosicion += 1

    # podría poner todas las otras cosas de los sll en la clase dll pero creo que ya lo entendí
