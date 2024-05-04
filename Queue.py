class Node:

    def __init__(self, val):
        self.data = val
        self.next = None


class Queue:

    def __init__(self):
        self.front = None
        self.rare = None

    def enqueue(self, val):
        new_node = Node(val)
        if self.is_empty():
            self.front = new_node
            self.rare = self.front
        else:
            self.rare.next = new_node
            self.rare = new_node

    def dequeue(self):

        if self.front is None:
            return 'Empty'
        else:
            self.front = self.front.next

    def travrse(self):

        temp = self.front

        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next

    def is_empty(self):
        return self.front is None

    def size(self):
        temp = self.front
        counter = 0
        while temp is not None:
            counter += 1
            temp = temp.next
        return counter
    def front_item(self):
        if self.is_empty():
            return 'Empty'
        else:
            return self.front.data
    def rare_item(self):
        if self.is_empty():
            return 'Empty'
        else:
            return self.rare.data

q = Queue()
q.enqueue(2)
q.enqueue(29)
q.enqueue(7)
q.enqueue(3)
q.enqueue(43)
q.dequeue()
q.travrse()
