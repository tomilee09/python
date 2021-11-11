from double_linked_list import DoubleLinkedList

dll = DoubleLinkedList()
dll.add(1)
dll.add(2)
dll.add(3)
dll.add(4)
dll.add(5)

dll.print()

# hago los next() solo pa mostrar el texto del print
dll.next()
dll.next()
print(
    f'las referencias de {dll.posicion.valor} son atras: {dll.posicion.refAtras.valor} y delante: {dll.posicion.refDelante.valor}')
