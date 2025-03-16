# Assignment-5: Circular Linked List

""" # 1. Define a class Node to describe a node of a circular linked list.
class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next """

""" # 2. Define a class CLL to implement Circular Linked List with _init_() method to create and initialise last reference variable.
class CLL:
    def __init__(self,last=None):
        self.last=last """

""" # 3. Define a method is_empty() to check if the linked list is empty in CLL class.
    def is_empty(self):
        return self.last==None """

""" # 4. In class CLL, define a method insert_at_start() to insert an element at the starting of the list.
    def insert_at_start(self,data):
        newnode=Node(data)
        if self.is_empty():
            self.last=newnode
            self.last.next=self.last
        else:
            newnode.next=self.last.next
            self.last.next=newnode """

""" # 5. In class CLL, define a method insert_at_last() to insert an element at the end of the list.
    def insert_at_last(self,data):
        newnode=Node(data)
        if self.is_empty():
            self.last=newnode
            self.last.next=self.last
        else:
            newnode.next=self.last.next
            self.last.next=newnode
            self.last=newnode """

""" # 6. In class CLL, define a method search() to find the node with specified element value.
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
        return False """

""" # 7. In class CLL, define a method insert_after() to insert a new node after a given node of the list.
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
                self.last=newnode """

""" # 8. In class CLL, define a method to print all the elements of the list.
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
        print() """

""" # 9. In class CLL, implement iterator for CLL to access all the elements of the list in a sequence.
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
        return data """
    
""" # 10. In class CLL, define a method delete_first() to delete first element from the list.
    def delete_first(self):
        if self.is_empty():
            return
        if self.last==self.last.next:
            self.last=None
        else:
            self.last.next=self.last.next.next """

""" # 11. In class CLL, define a method delete_last() to delete last element from the list.
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
            self.last=t """

""" # 12. In class CLL, define a method delete_item() to delete specified element from the list.
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
        return CLLIterator(self.last) """
