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

    def remove_max(self,item):
        temp =self.head
        max = temp
        while temp.next != None:
            if (temp.data > max.data) :
                max = temp
            temp = temp.next
        max.data= item


l=LinkedList()
l.insert_head(1)
l.insert_head(2)
l.insert_head(3)
l.insert_head(4)
l.remove_max(6)
# print(l.max())
print(l)




