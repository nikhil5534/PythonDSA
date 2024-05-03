class Node ():
    def __init__(self,value):
        self.data = value
        self.next = None
class Stack ():
    def __init__(self):
        self.top = None
        self.n = 0
    def isempty(self):
        return self.top == None
    def push(self,value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.n += 1
    def pop(self):
        if Stack.isempty(self):
            print('Empty Stack ')
        else:
            data = self.top.data
            self.top = self.top.next
            self.n -= 1
            return data
    def traverse(self):
        temp = self.top
        while temp != None:
            print(temp.data)
            temp = temp.next
    def peek(self):
        if Stack.isempty(self):
            return "Stack Empty"
        return print(f"Top is {self.top.data}")
    def size(self):
        return print(self.n)
#     reverse string using stack
    def reverse_str(self,string):
        temp =self.top
        res = ""
        for i in string :
            self.push(i)
        while (not self.isempty()):
            res =res +self.pop()
        return res



s = Stack()
# s.push(213)
# s.push(211)
# s.push(22)
# s.push(213)
# s.push(243)
# s.push(3)
# s.push(24)
# s.pop()
print(s.reverse_str("HELLO"))
# print(s.isempty())
# s.peek()
# s.size()
# s.traverse()