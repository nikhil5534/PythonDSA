class Dictionary:

    def __init__(self, size):
        self.size = size
        self.slot = [None] * self.size  # key
        self.data = [None] * self.size  # Value


    def put(self, key, value):
        hash_value = self.hash_function(key)

        if self.slot[hash_value] is None:
            self.slot[hash_value] = key
            self.data[hash_value] = value

        else:
            if self.slot[hash_value] == key:  # Use == instead of is for value comparison
                self.data[hash_value] = value
            else:
                new_hash = self.rehash(hash_value)
                while self.slot[new_hash] is not None and self.slot[new_hash] != key:  # Update to new_hash
                    new_hash = self.rehash(new_hash) # Update hash_value to new_hash

                if self.slot[new_hash] is None:
                    self.slot[new_hash] = key
                    self.data[new_hash] = value

                else:
                    self.data[new_hash] = value

    def __setitem__(self, key, value):
        self.put(key, value)

    def get(self, key):
        start = self.hash_function(key)
        curr = start

        while self.slot[curr] is not None:
            if self.slot[curr] == key:
                return self.data[curr]
            curr = self.rehash(curr)
            if curr == start:
                return "Not Found"
        return "Not Found"
    def __getitem__(self, item):
        return self.get(item)
    def __str__(self):
        for i in range(len(self.slot)):
            if self.slot[i] is not None:
                print(self.slot[i],":",self.data[i], end=' ')
        return ''
    def dell(self,key):
        start = self.hash_function(key)
        curr = start

        while self.slot[curr] is not None:
            if self.slot[curr] == key:
                self.slot[curr] = None
                self.data[curr] = None
            curr = self.rehash(curr)
            if curr == start:
                return "Not Found"
        return "Not Found"

    def rehash(self, old_hash):
        return (old_hash + 1) % self.size  # Use modulo operator to ensure index is within range

    def hash_function(self, key):
        return abs(hash(key)) % self.size  # Use modulo operator to ensure index is within range


D1 = Dictionary(3)
print(D1.slot)
print(D1.data)
D1['python'] = 32
D1['java'] = 35
D1['php'] = 34
# D1['ph'] = 34
print(D1.get('jav'))
D1.dell('python')
D1['hell'] = 11
print(D1.slot)
print(D1.data)
print(D1)
