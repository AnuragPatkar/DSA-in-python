# Assignment-11: Stack Implementation by extending Singly Linked List

""" # 1. Import module containing singly linked list code in your python file.
from singly_linked_list import * """

""" # 2. Define a class Stack to implement stack data structure by inheriting SLL class.
class Stack(SLL):
    def __init__(self):
        super().__init__()
        self.item_count=0 """

""" # 3. Define a method is_empty() to check if the stack is empty in Stack class.
    def is_empty(self):
        return super().is_empty() """

""" # 4. In Stack class, define push() method to add data onto the stack.
    def push(self,data):
        self.insert_at_start(data)
        self.item_count+=1 """

""" # 5. In Stack class, define pop() method to remove top element from the stack.
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        else:
            self.delete_first()
            self.item_count-=1 """

""" # 6. In Stack class, define peek() method to return top element on the stack.
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        else:
            return self.start.item """

""" # 7. In Stack class, define size() method to return size of the stack that is number of items present in the stack.
    def size(self):
        return self.item_count """