class Dictionary:

    def __init__(self, size):
        self.size = size
        self.slot = [None]*self.size  # key
        self.data = [None]*self.size  # Value

    def put(self, key, value):

        hash_value = self.hash_function(key)
        if self.slot[hash_value] is None:
            self.slot[hash_value] = key
            self.data[hash_value] = value
        else:
            if self.slot[hash_value] is key:
                self.data[hash_value] = value
            new_hash = self.rehash(hash_value)
            while self.slot[hash_value] is not None and self.slot[hash_value] is not key:
                new_hash = self.rehash(new_hash)
            if self.slot[new_hash] is None:
                self.slot[new_hash] = key
                self.data[new_hash] = value
            else:
                self.data[new_hash] = value

    def rehash(self, old_hash):

        return (old_hash + 1) % self.size

    def hash_function(self, key):
        return abs(hash(key))


D1 = Dictionary(3)
print(D1.slot)
print(D1.data)
