import ctypes

class MeraList:
    def __init__(self):
        self.size = 1
        self.n = 0
        # Create a C type array with size = self.size
        self.A = self._make_array(self.size)

    def __len__(self):
        return self.n

    def append(self, item):
        if self.n == self.size:
            # Resize
            self._resize(self.size * 2)

        # Append
        self.A[self.n] = item
        self.n += 1
    def insert(self,pos,item):
        if self.n== self.size:
            self._resize(self.size*2)
        for i in(self.n,pos,-1):
            self.A[i]=self.A[i-1]
        self.A[pos]=item
        self.n=self.n+1
    def _resize(self, new_capacity):
        # Create a new array with new capacity
        B = self._make_array(new_capacity)
        self.size = new_capacity
        # Copy the content of A to B
        for i in range(self.n):
            B[i] = self.A[i]
        # Reassign A
        self.A = B

    def __str__(self):
        result = ''
        for i in range(self.n):
            result += str(self.A[i]) + ','
        return '[' + result[:-1] + ']'
    def pop(self):
        if self.n==0 :
            return 'Empty List'
        print(self.A[self.n-1])
        self.n=self.n-1
    def __delitem__(self,pos):
        if 0<= pos < self.n:
            for i in range (pos,self.n-1):
                self.A[i]=self.A[i+1]

            self.n=self.n-1
    def remove(self,item):
        a= self.find(item)
        if type(a)== int:
            self.__delitem__(a)
        else:
            print('ValueError-Not Found')

    def clear(self):
        self.n=0
        self.size=1
    def __getitem__(self, index):
        if 0<= index <self.n:
            return self.A[index]
        else:
            return 'Index Error - Index Out of range'
    def find(self,item):
        for i in range(self.n):
            if self.A[i] == item:
                return i
        return 'ValueError-Not Found'
    def _make_array(self, capacity):
        # Creates a C type array(static, refrential) with size capacity
        return (capacity * ctypes.py_object)()
l = MeraList()
l.append(1)
l.append(2)
l.append(3)
l.remove(6)
print(l)
l.insert(2,43)
print(l.find(6))
l.pop()
del l[0]
print(l[0])
l.clear()
