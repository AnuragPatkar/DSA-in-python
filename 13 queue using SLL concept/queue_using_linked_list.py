from singly_linked_list import *
class Queue:
    def __init__(self):
        self.mylist=SLL()

    def is_empty(self):
        return self.mylist.is_empty()
    
    def enqueue(self,data):
        self.mylist.insert_at_last(data)

    def dequeue(self):
        if self.mylist.is_empty():
            raise IndexError("Queue is empty")
        else:
            self.mylist.delete_first()

    def getFront(self):
        if self.mylist.is_empty():
            raise IndexError("Queue is empty")
        else:
            return self.mylist.start.item
        
    def getRear(self):
        if self.mylist.is_empty():
            raise IndexError("Queue is empty")
        else:
            t=self.mylist.start
            while t.next is not None:
                t=t.next
            return t.item
        
    def size(self):
        t=self.mylist.start
        count=0
        while t is not None:
            count+=1
            t=t.next
        return count
    
q1=Queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
print(q1.getFront())
print(q1.getRear())
q1.dequeue()
print(q1.getFront())
print(q1.getRear())
print(q1.size())
