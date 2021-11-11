# Los queue son lo contrario a los stacks, lo primero en entrar es lo primero en salir
# es como una fila de una tienda, si llegas primero a la fila te van a atender primero
# Los queue se pueden hacer con listas, nodos o 2 stacks, voy a hacerlo de todas ellas

import sys
sys.path.append("../nodos/")
sys.path.append("../stack/")
from nodos import Nodo
from stack import Stack
import copy

class QueueListas:
    """Clase de queue hecha con listas """

    def __init__(self):
        self.lista = []

    def add(self, elemento):
        self.lista.append(elemento)

    def pop(self):
        self.lista.pop(0)

    def print(self):
        print(self.lista)


class QueueNodos:
    """Clase de queue hecha con nodos """

    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0

    def head(self):
        """ esta la hago pa no reutilizar código, la función me entrega el último nodo """
        if self.tail != None:
            self.head = self.tail
            while self.head.referencia:
                self.head = self.head.referencia
            return self.head

    def add(self, valor):
        """agrega un nodo al final"""
        nodoAgregar = Nodo(valor)

        if self.tail == None:
            self.tail = nodoAgregar

        else:
            lastNodo = QueueNodos.head(self)
            lastNodo.referencia = nodoAgregar

    def pop(self):
        """hago que self.tail equivalga al nodo siguiente, con lo cual self.tail apunta directamente al nodo subsiguiente y mantiene el valor del segundo nodo, así que es como si el segundo nodo no existiese (no se pasa por él)"""
        self.tail.valor = self.tail.referencia.valor
        self.tail.referencia = self.tail.referencia.referencia

    def print(self):
        """muestra en pantalla todo el queue"""
        # si la sll está vacia entonces mostramos un mensaje
        if self.tail == None:
            print("queue is empty")

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


class queueStacks:
    """Sabemos que los stack son lo contrario a un queue, pero si tenemos 2 stacks podemos unir ambos y obtener un queueStack
        Esto se realiza esperando a que uno de los stacks reciba todos los elementos y en ese punto pasa todos sus elementos 
        al otro stack, haciendo que el orden de los elementos se invierta y obteniendo un queue """
    def __init__(self):
        self.stackIn = Stack() 
        self.stackOut = Stack() 

    def add(self, elemento):
        self.stackIn.add(elemento)

    def pop(self):
        copiaStackIn = copy.deepcopy(self.stackIn)
        for i in range(self.stackIn.size-1):
            elemento_sacado = self.stackIn.pop() # aqui elimino el elemento y lo tomo 
            self.stackOut.add(elemento_sacado.valor) ######### AQUI ESTÁ EL ERROR, COMO LO AGREGO 2 VECES TENGO UN NODO DENTRO DE OTRO
        #self.stackOut.pop()
        self.stackIn = copiaStackIn

    def printAmbosStacks(self):
        print("stackIn: ")
        self.stackIn.print()
        print("stackOut: ")
        self.stackOut.print()

    def print(self):
        self.stackOut.print()