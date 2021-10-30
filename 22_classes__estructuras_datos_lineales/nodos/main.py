from nodos import Nodo  

nodo1 = Nodo("valor nodo 1", None)
nodo2 = Nodo("este es un valor del nodo 2", nodo1)
nodo3 = Nodo("hola nodo 1 :)", nodo2)
print(nodo1.valor) 
print(nodo2.referencia.valor) # obtuve el valor del nodo 1 a partir del nodo 2
print(nodo3.referencia.valor) # valor del nodo 2 a partir del nodo 3

# lo anterior es un conjunto de datos con direcciones, es como un grafo
# las direcciones van así:
# nodo1 <- nodo2 <- nodo3
# aunque no es necesario que las direcciones sean secuenciales