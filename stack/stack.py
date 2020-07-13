from singly_linked_list import LinkedList
"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 
1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
# array method

# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         self.storage.append(value)

#     def pop(self):
#         if self.storage:
#             return self.storage.pop()

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        l = 0
        if self.storage.head:
            l = 1
            curr = self.storage.head
            while curr.get_next() is not None:
                l += 1
                curr = curr.get_next()
        return l

    def push(self, value):
        self.storage.add_to_tail(value)

    def pop(self):
        if self.storage:
            return self.storage.remove_head()