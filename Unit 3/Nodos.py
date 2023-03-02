class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def setData(self, dato):
        self.data = dato


nodo1 = Node("Jesus")
print(nodo1.data)
print(nodo1.getData())
print(nodo1.next)

nodo1.setData("María")
print(nodo1.getData())
print(nodo1.data)

nodo2 = Node("Jose")

nodo1.next = nodo2 # type: ignore
print(nodo1.data)

nodo3=Node("Jesus")
nodo2.next =nodo3 # type: ignore

print("-------------")
print(nodo1.data)
print(nodo1.next.data)
print(nodo1.next.next.data) # type: ignore
print(nodo1.next.next.next) # type: ignore