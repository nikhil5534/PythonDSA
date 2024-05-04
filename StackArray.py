class Stack:
    def __init__(self, size):
        self.size = size
        self.__stack = [None] * self.size
        self.top = -1

    def push(self, value):
        if self.top == self.size - 1:
            return print(f'Overflow for {value}')
        else:
            self.top += 1
            self.__stack[self.top] = value

    def pop(self):
        if self.top == -1:
            return print("Empty")
        else:
            data = self.__stack[self.top]
            self.top -= 1
            print(data)

    def traverse(self):
        for i in range(self.top + 1):
            print(self.__stack[i], end=" ")


s = Stack(3)
s.push(2)
s.push(3)
s.push(7)
s.push(4)
s.pop()
s.pop()
s.pop()
s.pop()
s.traverse()

