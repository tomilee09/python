import sys
sys.path.append("../array/") # para que encuentre los archivos de esa carpeta
from clase_array import Array

class Array2d:
    def __init__(self, x, y, valor_inicial = 0):
        self.array2d = Array(x)
        for i in range(x):
            self.array2d.cambiarValor(i, Array(y))
            

    def numero_filas(self):
        return self.array2d.largo()


    def numero_columnas(self):
        return self.array2d.tomarElemento(0).largo()


    def seleccionar_elemento(self, x, y):
        return self.array2d.tomarElemento(x).tomarElemento(y)


    def cambiar_elemento(self, x, y, valor):
        self.array2d.tomarElemento(x).cambiarValor(y, valor)


    def imprimir(self):
        texto_impreso = ""
        texto_impreso += "["
        for i in range(self.numero_filas()):
            texto_impreso += "["
            for j in range(self.numero_columnas()):
                texto_impreso += f', {self.array2d.tomarElemento(i).tomarElemento(j)}' if j != 0 else f'{self.array2d.tomarElemento(i).tomarElemento(j)}'
            texto_impreso += "], \n" if i != self.numero_filas()-1 else "]"
        texto_impreso += "]"
        return texto_impreso