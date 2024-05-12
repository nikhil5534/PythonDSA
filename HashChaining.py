class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.n = 0

    def __len__(self):
        return self.n

    def traverse(self):
        curr = self.head
        while curr:
            print(curr.key, '-->', curr.value, ' ', end=" ")
            curr = curr.next

    def append(self, key, value):
        new_node = Node(key, value)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
        self.n += 1

    def clear(self):
        self.head = None
        self.n = 0

    def delete_head(self):
        curr = self.head
        if curr.next is None:
            print('Empty LinkedList')
        self.head = self.head.next
        self.n -= 1

    def remove(self, key):
        if self.head is None:
            return print('Empty LL')
        if self.head.key == key:
            self.delete_head()
            return
        else:
            curr = self.head
            while curr.next is None:
                if curr.next.key == key:
                    break
                curr = curr.next

            if curr.next is None:
                return print('Item Not found')
            else:
                curr.next = curr.next.next
                self.n -= 1

    def search(self, key):
        curr = self.head
        pos = 0
        while curr is not None:
            if curr.key == key:
                return pos
            curr = curr.next
            pos = pos+1

        return -1

    def get_node_at_index(self, index):
        curr = self.head
        pos = 0
        while curr is not None:
            if pos == index :
                return curr
            curr = curr.next
            pos = pos + 1


class Dictionary:

    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        # Create Array of Linked List
        self.buckets = self.make_array(self.capacity)

    def make_array(self, capacity):
        l = []
        # here loop is used instead of using l = [LinkedList()] because l = [LinkedList()] will
        # give same ll at other indexes hence we are creating new ll at every iteration
        for i in range(capacity):
            l.append(LinkedList())
        return l

    def put(self, key, value):
        bucket_index = hash(key)
        node_index = self.get_node_index(bucket_index, key)
        if node_index == -1:
            # insert
            self.buckets[bucket_index].append(key, value)
            self.size += 1
        else:
            # update
            node = self.buckets[bucket_index].get_node_at_index(node_index)
            node.value = value

    def get_node_index(self, bucket_index, key):
        return self.buckets[bucket_index].search(key)

    def hash(self, key):
        return abs(hash(key)) % self.capacity




