class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.n = 0

    def __len__(self):
        return self.n

    def insert_head(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.n += 1

    def __str__(self):
        curr = self.head
        result = ''
        while curr:
            result += str(curr.data) + "->"
            curr = curr.next
        return result[:-2]
    def oddSum(self):
        curr = self.head
        n = 0
        sum =0
        while curr.next != None:
            n =n+1
            curr =curr.next
            if n%2 != 0:
                sum =sum + curr.data
        return sum
l=LinkedList()
l.insert_head(1)
l.insert_head(2)
l.insert_head(3)
l.insert_head(4)
print(l.oddSum())


