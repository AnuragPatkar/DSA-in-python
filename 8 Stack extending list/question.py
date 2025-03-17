
# Assignment-8: Stack extending list

""" # 1. Define a class Stack to implement stack data structure by extending list class.
class Stack(list): """

""" # 2. Define a method is_empty() to check if the stack is empty in Stack class.
    def is_empty(self):
        return  len(self)==0 """

""" # 3. In Stack class, define push() method to add data onto the stack.
    def push(self,item):
        self.append(item) """

""" # 4. In Stack class, define pop() method to remove top element from the stack.
    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError("Stack is empty") """

""" # 5. In Stack class, define peek() method to return top element on the stack.
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("Stack is empty") """

""" # 6. In Stack class, define size() method to return size of the stack that is number of items present in the stack.
    def size(self):
        return len(self) """

""" # 7. Implement a way to restrict use of insert() method of list class from stack object
        def insert(self, index, data):
        raise AttributeError("NO insert function in Stack")  """