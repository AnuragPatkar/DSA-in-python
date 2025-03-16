class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class CLL:
    def __init__(self,last=None):
        self.last=last

    def is_empty(self):
        return self.last==None
    
    def insert_at_start(self,data):
        newnode=Node(data)
        if self.is_empty():
            self.last=newnode
            self.last.next=self.last
        else:
            newnode.next=self.last.next
            self.last.next=newnode

    def insert_at_last(self,data):
        newnode=Node(data)
        if self.is_empty():
            self.last=newnode
            self.last.next=self.last
        else:
            newnode.next=self.last.next
            self.last.next=newnode
            self.last=newnode

    def search(self,data):
        if self.is_empty():
            print("List is empty")
            return False
        t=self.last.next
        while True:
            if t.item==data:
                return True
            t=t.next
            if t==self.last.next:
                break
        return False

    def insert_after(self,key,data):
        if self.search(key):
            t=self.last.next
            while True:
                if t.item==key:
                    break
                t=t.next
            newnode=Node(data)
            newnode.next=t.next
            t.next=newnode
            if t.next==self.last.next:
                self.last=newnode

    def print_item(self):
        if self.is_empty():
            print("List is empty")
            return
        t=self.last.next
        while True:
            print(t.item, end=' ')
            t=t.next
            if t == self.last.next:
                break
        print()

    def delete_first(self):
        if self.is_empty():
            return
        if self.last==self.last.next:
            self.last=None
        else:
            self.last.next=self.last.next.next

    def delete_last(self):
        if self.is_empty():
            return
        if self.last==self.last.next:
            self.last=None
        else:
            t=self.last.next
            while t.next!=self.last:
                t=t.next
            t.next=self.last.next
            self.last=t
   
    def delete_item(self,data):   
        if self.search(data):
            if self.last.next.item==data:
                self.delete_first()
            else:
                t=self.last.next
                while True:
                    if t.next.item==data:
                        break
                    t=t.next
                t.next=t.next.next
                
    def __iter__(self):
        return CLLIterator(self.last)
    
class CLLIterator:
    def __init__(self, last):
        self.start = last.next if last else None
        self.current = self.start
        self.last = last
        self.first_pass = True
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.current or (self.current == self.start and not self.first_pass):
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        if self.current == self.start:
            self.first_pass = False
        return data


            
    


c1=CLL()
c2=CLL()
c1.insert_at_start(10)
c1.insert_at_start(20)
c1.insert_at_start(30)
c1.insert_at_last(40)
c1.insert_at_last(50)
print(c1.search(10))
print(c1.search(100))

c1.insert_after(20,55)
c1.insert_after(30,35)
c1.insert_after(50,55)
c1.print_item()

c1.delete_first()
c1.print_item()

c1.delete_last()
c1.print_item()

c1.delete_item(55)
c1.print_item()

for x in c1:
    print(x,end=' ')
print()

c2.insert_at_start(55)
c2.print_item()
c2.delete_first()
c2.print_item()

            
