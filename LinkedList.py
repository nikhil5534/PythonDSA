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

    def insert_head(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.n += 1

    def __str__(self):
        curr = self.head
        result = ''
        while curr:
            result += str(curr.data) + "->"
            curr = curr.next
        return result[:-2]

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

    def insert_after(self, after, value):
        new_node = Node(value)
        curr = self.head
        while curr:
            if curr.data == after:
                break
            curr = curr.next
        if curr:
            new_node.next = curr.next
            curr.next = new_node
            self.n += 1
        else:
            return 'Item not found'

    def clear(self):
        self.head = None
        self.n = 0

    def delete_head(self):
        curr = self.head
        if (curr.next == None):
            print('Empty LinkedList')
        self.head = self.head.next
        self.n -= 1
    def delete_tail(self):
        if self.head == None:
            return 'Empty LL'
        curr = self.head
        if curr.next == None:
            return self.delete_head()
        else:
            while curr.next.next!=None:
                curr = curr.next
            curr.next = curr.next.next
            self.n -= 1
    def remove(self,value):
        if self.head == None:
            return print('Empty LL')
        if self.head.data == value:
            return self.delete_head()
        curr=self.head
        while curr.next != None:
             if curr.next.data ==value:
                 break
             curr=curr.next

        if curr.next == None:
            return print('Item Not found')
        else:
            curr.next=curr.next.next
            self.n -= 1

    def search(self,item):
        curr=self.head
        pos =0
        while curr != None:
            if curr.data == item:
                return pos
            curr =curr.next
            pos=pos+1

        return print('Item Not Found')
    def __getitem__(self, item):
        curr = self.head
        pos = 0
        while curr != None:
            if pos == item:
                return curr.data
            curr = curr.next
            pos = pos + 1

        return print('IndexError')

    # #for same niche wala bhi hai
    # def item(self,index):
    #     curr=self.head
    #     while curr.next != None:
    #         if self.search(curr.data) == index:
    #             return print(curr.data)
    #         curr =curr.next
    #     if self.search(curr.data) == index:
    #             return print(curr.data)
    #     return print('IndexError')

# Example usage


l = LinkedList()
l.insert_head(1)
l.insert_head(2)
l.insert_head(3)
l.insert_head(4)
l.item(0)
print(l)
# l.search(20)
# l.remove(12)
# l.insert_head(7)
# l.append(5)
# l.append(9)
# # l.delete_tail()
# # l.delete_head()
# # l.clear()
# print(len(l))
# print(l)
# print(l.insert_after(34, 23))  # Insert 23 after 4

