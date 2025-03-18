from Doubly_linked_list import *
class Deque:
    def __init__(self):
        self.mylist=DLL()

    def is_empty(self):
        return self.mylist.is_empty()
    
    def insert_front(self,data):
        self.mylist.insert_at_start(data)

    def insert_rear(self,data):
        self.mylist.insert_at_last(data)

    def delete_front(self):
        if self.mylist.is_empty():
            raise IndexError("Deque is empty")
        else:
            self.mylist.delete_first()

    def delete_rear(self):
        if self.mylist.is_empty():
            raise IndexError("Deque is empty")
        else:
            self.mylist.delete_last()

    def get_front(self):
        if self.mylist.is_empty():
            raise IndexError("Deque is empty")
        else:
            return self.mylist.start.item
    
    def get_rear(self):
        if self.mylist.is_empty():
            raise IndexError("Deque is empty")
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

    
d1=Deque()
print(d1.is_empty())
d1.insert_front(10)
d1.insert_front(20)
d1.insert_front(30)
d1.insert_front(40)
d1.insert_rear(100)       
d1.insert_rear(90)       
d1.insert_rear(80)
print(d1.get_front())       
print(d1.get_rear())
d1.delete_front()
d1.delete_rear()
print(d1.get_front())       
print(d1.get_rear())
print(d1.size())
