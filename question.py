#Assignment-4: Doubly Linked List

""" # 1. Define a class Node to describe a node of a doubly linked list.
class Node:
    def __init__(self,item=None,prev=None,next=None):
        self.item=item
        self.prev=prev
        self.next=next """

""" # 2. Define a class DLL to implement Doubly Linked List with _init_() method to create and initialise start reference variable.
class DLL:
    def __init__(self,start=None):
        self.start=start """

""" # 3. Define a method is_empty() to check if the linked list is empty in DLL class.
    def is_empty(self):
        return self.start==None """

""" # 4. In class DLL, define a method insert_at_start() to insert an element at the starting of the list.
    def insert_at_start(self,data):
        newnode=Node(data)
        if self.is_empty():
            self.start=newnode
        else:
           newnode.next=self.start
           self.start.prev=newnode
           self.start=newnode """

""" # 5. In class DLL, define a method insert_at_last() to insert an element at the end of the list.
    def insert_at_last(self,data):
        newnode=Node(data)
        if self.is_empty():
            self.start=newnode
        else:
            t=self.start
            while t.next is not None:
                t=t.next
            t.next=newnode
            newnode.prev=t """

""" # 6. In class DLL, define a method search() to find the node with specified element value.
    def search(self,data):
        if self.is_empty():
            return False
        t=self.start
        while t is not None:
            if t.item==data:
                return True
            t=t.next
        return False  """ 

""" # 7. In class DLL, define a method insert_after() to insert a new node after a given node of the list.
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
            newnode.prev=t """

""" # 8. In class DLL, define a method to print all the elements of the list.
    def print_item(self):
        t=self.start
        while t is not None:
            print(t.item,end=' ')
            t=t.next
        print() """

""" # 9. In class DLL, implement iterator for DLL to access all the elements of the list in a sequence.
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
        return data """

""" # 10. In class DLL, define a method delete_first() to delete first element from the list.
    def delete_first(self):
        if self.is_empty():
            return
        self.start=self.start.next
        if self.start is not None:
            self.start.prev=None """

""" # 11. In class DLL, define a method delete_last() to delete last element from the list.
    def delete_last(self):
        if self.is_empty():
            return
        if self.start.next is None:
            self.delete_first()
        else:
            t=self.start
            while t.next.next is not None:
                t=t.next
            t.next=None """

""" # 12. In class DLL, define a method delete_item() to delete specified element from the list
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
                    t.next=None """