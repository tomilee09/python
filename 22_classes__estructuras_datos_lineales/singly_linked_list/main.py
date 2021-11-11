from singly_linked_list import SinglyLinkedList

sll = SinglyLinkedList()
sll.add(1)
sll.add(2)
sll.add(3)
sll.add(4)
sll.add(5)
sll.addList([6, 7, 8])
sll.print()

# aqui trabajo con la posicion
sll.showPosicion()
sll.next()
sll.showPosicion()
sll.next()
sll.showPosicion()
sll.next()
sll.showPosicion()
sll.next()
sll.showPosicion()
sll.next()
sll.showPosicion()
sll.next()
sll.showPosicion()
sll.next()
sll.showPosicion()

# si hubiera puesto otro next() hubiera dado error por no haber más elementos, pero si esta sll fuera circular podría hacer más
sll.sll2circular()
sll.next()
sll.showPosicion()
sll.next()
sll.showPosicion()
sll.circular2sll()  # lo devuelvo a una sll

# además puedo agregar un elemento en la posicion donde se encuentre self.posicion
print("antes de insertar")
sll.print()
sll.insert(999)
print("despues de insertar")
sll.print()

# además puedo borrar elementos
print("antes de borrar")
sll.print()
sll.erase()
print("despues de borrar")
sll.print()
