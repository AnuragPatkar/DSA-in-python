from Singly_linked_list import *
class Stack:
    def __init__(self):
        self.mylist=SLL()
        self.count=0

    def is_empty(self):
        return self.mylist.is_empty()
    
    def push(self,data):
        self.mylist.insert_at_start(data)
        self.count +=1

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        else:
            t=self.mylist.start.item
            self.mylist.delete_first()
            self.count-=1
            return t
        
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        else:
            return self.mylist.start.item
        
    def size(self):
        return self.count
    
s1=Stack()
s1.push(10)
s1.push(20)
s1.push(30)
print(s1.peek())
print(s1.is_empty())
print(s1.pop())
print(s1.peek())
print(s1.size())
        


