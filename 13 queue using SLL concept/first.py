class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class Queue:
    def __init__(self,front=None,rear=None):
        self.front=front
        self.rear=rear
        self.item_count=0
    
    def is_empty(self):
        return self.rear==None
    
    def enqueue(self,data):
        newnode=Node(data)
        if self.is_empty():
            self.front=newnode
            self.rear=newnode
        else:
            self.rear.next=newnode
            self.rear=newnode
        self.item_count+=1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        elif self.front==self.rear:
            self.rear=None
            self.front=None
            self.item_count-=1
        else:
            self.front=self.front.next
            self.item_count-=1
    
    def getFront(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        else:
            return self.front.item
    
    def getRear(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        else:
            return self.rear.item
        
    def size(self):
        return self.item_count
    
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



    
