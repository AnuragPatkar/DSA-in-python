class Node:
    def __init__(self,item=None,prev=None,next=None):
        self.item=item
        self.prev=prev
        self.next=next
        
class DLL:
    def __init__(self,start=None):
        self.start=start
    
    def is_empty(self):
        return self.start==None
    
    def insert_at_start(self,data):
        newnode=Node(data)
        if self.is_empty():
            self.start=newnode
        else:
           newnode.next=self.start
           self.start.prev=newnode
           self.start=newnode

    def insert_at_last(self,data):
        newnode=Node(data)
        if self.is_empty():
            self.start=newnode
        else:
            t=self.start
            while t.next is not None:
                t=t.next
            t.next=newnode
            newnode.prev=t
    
    def search(self,data):
        if self.is_empty():
            return False
        t=self.start
        while t is not None:
            if t.item==data:
                return True
            t=t.next
        return False    
        
    def insert_after(self,key,data):
        if self.is_empty():
            print(key,"not found")
            return
        if self.search(key):
            newnode=Node(data)
            t=self.start
            while t is not None:
                if t.item==key:
                    break
                t=t.next
            if t.next is not None:
                t.next.prev=newnode
                newnode.next=t.next
            t.next=newnode
            newnode.prev=t
    
    def print_item(self):
        t=self.start
        while t is not None:
            print(t.item,end=' ')
            t=t.next
        print()

    def delete_first(self):
        if self.is_empty():
            return
        self.start=self.start.next
        if self.start is not None:
            self.start.prev=None

    def delete_last(self):
        if self.is_empty():
            return
        if self.start.next is None:
            self.delete_first()
        else:
            t=self.start
            while t.next.next is not None:
                t=t.next
            t.next=None
        
    def delete_item(self,data):
        if self.search(data):
            if self.start.item==data:
                self.delete_first()
            else:
                t=self.start
                while t.next.item !=data:
                    t=t.next
                if t.next.next is not None:
                    t.next=t.next.next
                else:
                    t.next=None
    
    def __iter__(self):
        return DLLIterator(self.start)
    
class DLLIterator:
    def __init__(self,start):
        self.current=start

    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.current:
            raise StopIteration
        data=self.current.item
        self.current= self.current.next
        return data

#driver code
d1=DLL()
d1.insert_at_start(10)
d1.insert_at_start(20)
d1.insert_at_start(30)
d1.insert_at_start(40)
d1.insert_at_last(60)
d1.insert_at_last(70)
print(d1.search(30))
d1.insert_after(10,100)
d1.insert_after(70,100)

d1.print_item()
d1.delete_first()
d1.delete_last()
for x in d1:
    print(x,end=' ')
print()

d2=DLL()
d2.insert_at_start(50)
d2.insert_at_start(80)
d2.insert_at_start(100)
d2.print_item()
d2.delete_item(80)
d2.print_item()