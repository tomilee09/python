# los nodos son un tipo de dato que tiene un valor y una referencia
# podemos unir varios nodos creando una estructura de datos como 
# las SSL y las DLL (singly linked list y double linked list)
# aqui crearemos los nodos

class Nodo:
    def __init__(self, valor, referencia = None):
        self.valor = valor
        self.referencia = referencia
