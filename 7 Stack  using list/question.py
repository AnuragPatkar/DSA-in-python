# Assignment-7: Stack using list

""" # 1. Define a class Stack to implement stack data structure using list. Define init() method to create an empty list object as instance object member of Stack.
class Stack:
    def __init__(self):
        self.t = []
     """

""" # 2. Define a method is_empty() to check if the stack is empty in Stack class.
    def is_empty(self):
        return len(self.t) == 0 """

""" # 3. In Stack class, define push() method to add data onto the stack.
    def push(self, data):
        self.t.append(data) """

""" # 4. In Stack class, define pop() method to remove top element from the stack.
    def pop(self):
        if not self.is_empty():
            return self.t.pop()
        else:
            return None """

""" # 5. In Stack class, define peek() method to return top element on the stack.
    def peek(self):
        if self.is_empty():
            return "List is empty"
        else:
            return self.t[-1] """

""" # 6. In Stack class, define size() method to return size of the stack that is number of items present in the stack.
    def size(self):
        return len(self.t) """