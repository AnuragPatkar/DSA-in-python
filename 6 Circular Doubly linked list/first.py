class Node:
    def __init__(self,item=None,prev=None,next=None):
        self.item=item
        self.prev=prev
        self.next=next

class CDLL:
    def __init__(self, last=None):
        self.last = last

    def is_empty(self):
        return self.last==None
    
    def insert_at_start(self,data):
        newnode=Node(data)
        if self.is_empty():
            self.last=newnode
            self.last.next=self.last
            self.last.prev=self.last
        else:
            newnode.next=self.last.next
            self.last.next.prev=newnode
            self.last.next=newnode
            newnode.prev=self.last
   
    def insert_at_last(self,data):
        newnode=Node(data)
        if self.is_empty():
            self.last=newnode
            self.last.next=self.last
            self.last.prev=self.last
        else:
            newnode.next=self.last.next
            self.last.next.prev=newnode
            self.last.next=newnode
            newnode.prev=self.last
            self.last=newnode

    def search(self,data):
        if self.is_empty():
            return False
        t=self.last.next
        while True:
            if t.item==data:
                return True
            t=t.next
            if t==self.last.next:
                break
    
    def insert_after(self,key,data):
        if self.search(key):
            t=self.last.next
            while True:
                if t.item==key:
                    break
                t=t.next
            newnode=Node(data)
            t.next.prev=newnode
            newnode.next=t.next
            newnode.prev=t
            t.next=newnode
            if self.last.next==t.next:
                self.last=newnode

    def print_item(self):
        if self.is_empty():
            print("List is empty")
            return
        t=self.last.next
        while True:
            print(t.item,end=' ')
            t=t.next
            if t==self.last.next:
                break
        print()

    def delete_first(self):
        if self.is_empty():
            print("List is empty")
            return
        if self.last.next==self.last:
            self.last=None
        else:
            self.last.next=self.last.next.next
            self.last.next.prev=self.last

    def delete_last(self):
        if self.is_empty():
            return
        if self.last.next==self.last:
            self.last=None
        else:
            self.last.prev.next=self.last.next
            self.last.next.prev=self.last.prev
            self.last=self.last.prev
            
    def delete_item(self,data):
        if self.search(data):
            if self.last.item==data and self.last.next==self.last:
                self.last=None
                return
            t=self.last.next
            while t.item!=data:
                t=t.next
            t.prev.next=t.next
            t.next.prev=t.prev
            if t.next==self.last.next:
                self.last=t.prev

    def __iter__(self):
        return CDLLIterator(self.last)

class CDLLIterator:
    def __init__(self,last=None):
        self.start=last.next if last else None
        self.current=self.start
        self.last=last
        self.first_pass=True

    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.current or (self.current == self.start and not self.first_pass):
            raise StopIteration
        data=self.current.item
        self.current=self.current.next
        if self.current == self.start:
            self.first_pass = False
        return data
    
CD1=CDLL()
CD1.insert_at_start(10)
CD1.insert_at_start(20)
CD1.insert_at_start(30)
CD1.insert_at_last(40)
CD1.insert_at_last(50)
print(CD1.search(30))
CD1.print_item()

CD1.insert_after(40,100)
CD1.print_item()

CD1.delete_first()
CD1.delete_last()
CD1.print_item()
CD1.delete_item(100)

CD1.print_item()

for x in CD1:
    print(x,end=' ')
print()