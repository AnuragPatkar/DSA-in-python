class deque:
    def __init__(self):
        self.mylist=[]
    
    def is_empty(self):
        return len(self.mylist)==0
    
    def size(self):
        return len(self.mylist)
    
    def insert_front(self,data):
        self.mylist.insert(0,data)

    def insert_rear(self,data):
        self.mylist.append(data)

    def delete_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        else:
            self.mylist.pop(0)
    
    def delete_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        else:
            self.mylist.pop(-1)

    def get_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        else:
            return self.mylist[0]
        
    def get_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        else:
            return self.mylist[-1]

d1=deque()
print(d1.size())
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


    
