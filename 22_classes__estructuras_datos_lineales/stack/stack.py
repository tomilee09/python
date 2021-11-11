# al igual que con los sll, podemos crear la clase stack con nodos o listas, solo pa usar los nodos la voy a hacer con estos
# En los stacks el primer elemento en entrar es el primero en salir
# es como guardar cosas dentro de una caja, dado que hay solo una entrada, cuando vayas a sacar las cosas vas a sacar las últimas cosas que guardaste

import sys
sys.path.append("../nodos/")
from nodos import Nodo


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def add(self, elemento):
        """añade un elemento al stack"""
        nodo = Nodo(elemento)
        if self.size == 0:
            self.top = nodo
        else:
            posicion = self.top
            while posicion.referencia:
                posicion = posicion.referencia
            posicion.referencia = nodo
        self.size += 1

    def pop(self):
        """borra el último elemento añadido al stack"""
        posicion = self.top
        # dado que necesito llegar al penúltimo (pues debo cambiar la referencia) no me sirve el while, tengo que usar un for
        for i in range(self.size-2):
            posicion = posicion.referencia
        valor_a_retornar = posicion.referencia # esto para poder usar el nodo que saqué del stack
        posicion.referencia = None
        self.size -= 1
        return valor_a_retornar

    def print(self):
        """muestra en pantalla todo el stack"""
        # si la sll está vacia entonces mostramos un mensaje
        if self.top == None:
            print("Stack is empty")

        # si no está vacía mostramos los elementos
        else:
            i = self.top
            texto = ''
            while i:  # mientras exista un valor
                texto += str(i.valor)
                if i.referencia:  # si existe referencia entonces muestra una flechita
                    texto += '-->'
                i = i.referencia

            print(texto)
