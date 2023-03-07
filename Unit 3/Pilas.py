class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data


class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def getSize(self):
        return self.size

    def isEmpty(self):
        return True if self.size == 0 else False

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.head  # type:ignore
        self.head = newNode
        self.size += 1

    def pop(self):
        dato = None
        if not self.isEmpty():
            dato = self.head.data  # type:ignore
            self.head = self.head.next  # type:ignore
            self.size -= 1
        return dato

    def peek(self):
        return self.head.data  # type:ignore
    def show(self):
        mostrar = 
        return mostrar
q1 = Stack()
q1.push("Jesús")
q1.push("María")
q1.push("José")
print(q1.pop())
print(q1.peek())
print(q1.show())
