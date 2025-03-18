from singly_linked_list import *
class Stack(SLL):
    def __init__(self):
        super().__init__()
        self.item_count=0

    def is_empty(self):
        return super().is_empty()

    def push(self,data):
        self.insert_at_start(data)
        self.item_count+=1

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        else:
            self.delete_first()
            self.item_count-=1
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        else:
            return self.start.item
    
    def size(self):
        return self.item_count

s1=Stack()
s1.push(10)
s1.push(20)
s1.push(30)
print(s1.peek())
s1.pop()
print(s1.peek())
print(s1.size())