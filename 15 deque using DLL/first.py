class Node:
    def __init__(self,item=None,prev=None,next=None):
        self.item=item
        self.prev=prev
        self.next=next

class Deque:
    def __init__(self,front=None,rear=None):
        self.front=front
        self.rear=rear
        self.item_count=0

    def is_empty(self):
        return self.front is None
    
    def insert_front(self,data):
        newnode=Node(data)
        if self.is_empty():
            self.front=newnode
            self.rear=newnode
        else:
            self.front.prev=newnode
            newnode.next=self.front
            self.front=newnode
        self.item_count+=1

    def insert_rear(self,data):
        newnode=Node(data)
        if self.is_empty():
            self.front=newnode
            self.rear=newnode
        else:
            self.rear.next=newnode
            newnode.prev=self.rear
            self.rear=newnode
        self.item_count+=1       

    def get_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        else:
            return self.front.item
        
    def get_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        else:
            return self.rear.item
        
    def delete_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        elif self.front==self.rear:
            self.front=None
            self.rear=None
        else:
            self.front=self.front.next
            self.front.prev=None
        if self.item_count>0:
            self.item_count-=1

    def delete_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        elif self.front==self.rear:
            self.front=None
            self.rear=None
            self.item_count=0
        else:
            self.rear=self.rear.prev
            self.rear.next=None
        if self.item_count>0:
            self.item_count-=1    
    
    def size(self):
        return self.item_count
    
    def print_item(self):
        t=self.front
        while t is not None:
            print(t.item,end=' ')
            t=t.next
        print()
        

    
d1=Deque()
print(d1.is_empty())
d1.insert_front(10)
d1.insert_front(20)
d1.insert_front(30)
d1.insert_rear(100)
d1.insert_rear(90)
d1.insert_rear(80)
d1.print_item()

print(d1.get_front())
print(d1.get_rear())
d1.delete_front()
d1.delete_rear()
print(d1.get_front())
print(d1.get_rear())
print(d1.size())
d1.print_item()


