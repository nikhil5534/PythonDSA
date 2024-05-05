class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class Stack:

    def __init__(self):
        self.top = None
        self.n = 0

    def isempty(self):
        return self.top is not None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.n += 1

    def pop(self):
        if self.isempty():
            print('Empty Stack ')
        else:
            data = self.top.data
            self.top = self.top.next
            self.n -= 1
            return data

    def traverse(self):
        temp = self.top
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def size(self):
        return print(self.n)










