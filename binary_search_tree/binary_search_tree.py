from collections import deque
"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 
This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value >= self.value: #if input is bigger than self
            if self.right:#if right enter into right
                self.right.insert(value)
            else:#else make a node with given value to the right
                self.right = BSTNode(value)
        elif value < self.value: # if input is smaller
            if self.left: #if left enter into left
                self.left.insert(value)
            else: #else make node with given value 
                self.left = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value: #if value is the same as target return true
            return True
        if target < self.value: #if its less, check if there is something left; if not, return false, otherwise return left with target
            if not self.left:
                return False
            return self.left.contains(target)# return where target is in left
        else: #else, check if anything is right; if there is not, return false
            if not self.right:
                return False
            return self.right.contains(target)# return where target is in right
    # Return the maximum value found in the tree
    def get_max(self):
        if self.right: #largest will always be in the right, so if in left, return value, if in right, find the max value and return it
            return self.right.get_max()
        else:
            return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)#simply run fn then basically loop through both sides with for_each
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # in order traversal
        if node: #if there is a node, print left in order, then right in order
            self.in_order_print(node.left)
            print(node.value)
            self.in_order_print(node.right)
        

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = deque() #basically making a countdown of how many times to run function
        queue.append(node)

        while len(queue)>0:#while the queue isnt at 0
            current = queue.popleft()#makes it go left after printing given node
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            
            print(current.value)
            

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = []
        stack.append(node)

        while len(stack)>0: # same as bft except appending to list instead of starting with queue and counting down
            curr = stack.pop()
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
            print(curr.value)
            

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

x = BSTNode(10)
x.insert(8)
x.insert(7)
x.insert(3)
x.insert(11)
x.insert(13)
x.insert(16)

x.dft_print(x)