# Assignment-9: Stack using Linked List Concept

""" # 1. Define a class Stack to implement stack data structure using singly linked list concept. Define _init () method to initialise start reference variable and item_count variable to keep track of number of elements in the stack.
class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class Stack:
    def __init__(self,top=None):
        self.top=top """

""" # 2. Define a method is_empty() to check if the stack is empty in Stack class.
    def is_empty(self):
        return self.top==None """

""" # 3. In Stack class, define push() method to add data onto the stack.
    def push(self,data):
        newnode=Node(data)
        newnode.next=self.top
        self.top=newnode """

""" # 4. In Stack class, define pop() method to remove top element from the stack.
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        else:
            t=self.top.item
            self.top=self.top.next
            return t """

""" # 5. In Stack class, define peek() method to return top element on the stack.
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        else:
            return self.top.item """

""" # 6. In Stack class, define size() method to return size of the stack that is number of items present in the stack.
    def size(self):
        count=0
        t=self.top
        while t is not None:
            count +=1
            t=t.next
        return count """