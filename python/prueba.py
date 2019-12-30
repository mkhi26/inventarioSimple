from nucleo.LinkedList import *

l = LinkedList()
l.LinkedListAdd("Gato")
l.LinkedListAdd("Perro")
l.LinkedListAdd("Pez")
l.LinkedListAdd("Vaca")
l.LinkedListAdd("Pato")

p=l.LinkedListPrint()

print("Los elementos en la lista son: %s"%(p))

n = l.LinkedListSearch("Vaca")
print(n)

print("Se elimina el elemento %s"%(l.LinkedListPop(n).value))
p=l.LinkedListPrint()
print("Los elementos en la lista son: %s"%(p))

