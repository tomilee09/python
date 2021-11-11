class Nodo2:
    """son lo mismo que los nodos normales pero ahora tienen 2 referencias (las cuales usaré para ir para atras y adelante)"""

    def __init__(self, valor, refAtras=None, refDelante=None):
        self.valor = valor
        self.refAtras = refAtras
        self.refDelante = refDelante
