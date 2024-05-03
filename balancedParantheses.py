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
        return self.top.data
    def size(self):
        return self.n

def brackets(value):
    s =Stack()

    for i in value :
        if i in '({[':
            s.push(i)
        elif i ==')' and s.peek()=="(":
            s.pop()
        elif i ==']' and s.peek()=="[":
            s.pop()
        elif i =='}' and s.peek()=="{":
            s.pop()
        elif i in ')}]' and s.isempty():
            return False


    if s.isempty() or None:
        return True
    else:
        return False

c = '[{(a+b)+(c+d)}]'
print(brackets(c))