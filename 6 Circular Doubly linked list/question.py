# Assignment-6: Circular Doubly Linked List

""" # 1. Define a class Node to describe a node of a circular doubly linked list.
class Node:
    def __init__(self,item=None,prev=None,next=None):
        self.item=item
        self.prev=prev
        self.next=next """

""" # 2. Define a class CDLL to implement Circular Doubly Linked List with _init_() method to create and initialise last reference variable.
class CDLL:
    def __init__(self, last=None):
        self.last = last """

""" # 3. Define a method is_empty() to check if the linked list is empty in CDLL class.
    def is_empty(self):
        return self.last==None """

""" # 4. In class CDLL, define a method insert_at_start() to insert an element at the starting of the list.
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
            newnode.prev=self.last """

""" # 5. In class CDLL, define a method insert_at_last() to insert an element at the end of the list.
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
            self.last=newnode """

""" # 6. In class CDLL, define a method search() to find the node with specified element value.
    def search(self,data):
        if self.is_empty():
            return False
        t=self.last.next
        while True:
            if t.item==data:
                return True
            t=t.next
            if t==self.last.next:
                break """

""" # 7. In class CDLL, define a method insert_after() to insert a new node after a given node of the list.
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
                self.last=newnode """
                
""" # 8. In class CDLL, define a method to print all the elements of the list.
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
        print() """

""" # 9. In class CDLL, implement iterator for CDLL to access all the elements of the list in a sequence.
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
        return data """

""" # 10. In class CDLL, define a method delete_first() to delete first element from the list.
    def delete_first(self):
        if self.is_empty():
            print("List is empty")
            return
        if self.last.next==self.last:
            self.last=None
        else:
            self.last.next=self.last.next.next
            self.last.next.prev=self.last """

""" # 11. In class CDLL, define a method delete_last() to delete last element from the list.
    def delete_last(self):
        if self.is_empty():
            return
        if self.last.next==self.last:
            self.last=None
        else:
            self.last.prev.next=self.last.next
            self.last.next.prev=self.last.prev
            self.last=self.last.prev """

""" # 12. In class CDLL, define a method delete_item() to delete specified element from the list.
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
                self.last=t.prev """