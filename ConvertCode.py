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

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
        self.n += 1

    def __str__(self):
        curr = self.head
        result = ''
        while curr:
            result += str(curr.data)
            curr = curr.next
        return result
    def decode(self):
        temp = self.head
        while temp != None:
            if temp.data == '*' or temp.data == '/':
                temp.data = ' '
                if temp.next.data == '*' or temp.next.data == '/' :
                    temp.next.next.data =temp.next.next.data.capitalize()
                    temp.next = temp.next.next
            temp =temp.next



word_list = LinkedList()
word_list.append("T")
word_list.append("h")
word_list.append("e")
word_list.append("/")
word_list.append("*")
word_list.append("s")
word_list.append("k")
word_list.append("y")
word_list.append("*")
word_list.append("i")
word_list.append("s")
word_list.append("/")
word_list.append("/")
word_list.append("b")
word_list.append("l")
word_list.append("u")
word_list.append("e")
word_list.decode()
print(word_list)