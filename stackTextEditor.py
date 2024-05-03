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
def editor(text,pattern):
    u = Stack()
    r = Stack()

    for i in text :
        u.push(i)
    for i in  pattern:
        if i == 'u':
            a=u.pop()
            r.push(a)
        else:
            a =r.pop()
            u.push(a)
    res = ""
    while not u.isempty():
        res = u.pop() + res
    print(res)

editor("Hello","uurrur")