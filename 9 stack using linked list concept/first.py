class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class Stack:
    def __init__(self,top=None):
        self.top=top

    def is_empty(self):
        return self.top==None
    
    def push(self,data):
        newnode=Node(data)
        newnode.next=self.top
        self.top=newnode

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        else:
            t=self.top.item
            self.top=self.top.next
            return t
        
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        else:
            return self.top.item
        
    def size(self):
        count=0
        t=self.top
        while t is not None:
            count +=1
            t=t.next
        return count

s1=Stack()
s1.push(10)
s1.push(20)
s1.push(30)
print(s1.is_empty())
print(s1.peek())
print(s1.pop())
print(s1.peek())
print(s1.size())