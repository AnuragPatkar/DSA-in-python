
# Assignment-10: Stack using Linked List

""" # 1. Import module containing singly linked list code in your python file.
from Singly_linked_list import * """

""" # 2. Define a class Stack to implement stack data structure. Define _init__() method to create Singly Linked List (SLL) object.
class Stack:
    def __init__(self):
        self.mylist=SLL()
        self.count=0 """

""" # 3. Define a method is_empty() to check if the stack is empty in Stack class.
    def is_empty(self):
        return self.mylist.is_empty() """

""" # 4. In Stack class, define push() method to add data onto the stack.
    def push(self,data):
        self.mylist.insert_at_start(data)
        self.count +=1 """

""" # 5. In Stack class, define pop() method to remove top element from the stack.
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        else:
            t=self.mylist.start.item
            self.mylist.delete_first()
            self.count-=1
            return t """

""" # 6. In Stack class, define peek() method to return top element on the stack.
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        else:
            return self.mylist.start.item """

""" # 7. In Stack class, define size() method to return size of the stack that is number of items present in the stack.
    def size(self):
        return self.count """