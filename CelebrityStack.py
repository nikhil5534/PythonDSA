# in this problem a n*n matrix will be given as an input and celebrity be the person who don't know any
# any one but every one knows him known is represented by 1 unknown is represented by 0
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


L =[
    [0,0,0,0],
    [1,0,1,1],
    [0,0,0,0],
    [1,0,1,1]
]
def celebrity(L):
    s= Stack()
    # populate STACK
    for i in range (len(L)):
        s.push(i)
    while s.size() >= 2:
        i = s.pop()
        j = s.pop()

        if L[i][j] == 0:
            # j is not celebrity
            s.push(i)
        else:
            s.push(j)
    top = s.peek()
    print(top)
    for i in range (len(L)):
        if i != top:
            if L[top][i] == 1 or L[i][top] == 0:
                print("Celebrity not found")
                return
    print(f"{s.top.data} is celebrity ")
celebrity(L)