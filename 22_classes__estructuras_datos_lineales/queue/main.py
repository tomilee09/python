from queue import QueueListas
from queue import QueueNodos
from queue import queueStacks

###############Listas##############
print("queue con listas")
queue = QueueListas()
queue.add(1)
queue.add(2)
queue.add(3)
queue.add(4)
queue.add(5)
queue.pop()
queue.print()

###############Nodos##############
print("queue con nodos")
queue = QueueNodos()
queue.add(1)
queue.add(2)
queue.add(3)
queue.add(4)
queue.add(5)
queue.pop()
queue.print()

###############Stacks##############
print("queue con 2 stacks")
queue = queueStacks()
queue.add(1)
queue.add(2)
queue.add(3)
queue.add(4)
queue.add(5)
queue.pop()
queue.stackOut.print()
