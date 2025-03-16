# Assignment-3: Singly Linked List

""" # 1. Define a class Node to describe a node of a singly linked list.
class node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

 """

""" # 2. Define a class SLL to implement Singly Linked List with_init_() method to create and initialise start reference variable.
class SLL:
    def __init__(self, node=None):
        self.start = node """

""" # 3. Define a method is_empty() to check if the linked list is empty in SLL class.
    def is_empty(self):
        return self.start is None """

""" # 4. In class SLL, define a method insert_at_start() to insert an element at the starting of the list.
    def insert_at_start(self, x):
        new_node = Node(x)
        new_node.next = self.start
        self.start = new_node """

""" # 5. In class SLL, define a method insert_at_last() to insert an element at the end of the list.
    def insert_at_last(self, x):
        new_node = Node(x)
        if self.is_empty():
            self.start = new_node
        else:
            t = self.start
            while t.next is not None:
                t = t.next
            t.next = new_node """

""" # 6. In class SLL, define a method search() to find the node with specified element value.
  def search(self,x):
        if self.is_empty():
            return False
        t=self.start
        while t is not None:
            if t.item == x:
                return True
            t=t.next
        return False """

""" # 7. In class SLL, define a method insert_after() to insert a new node after a given node of the list.
def insert_after(self,key,x):
        if self.is_empty():
            print(key,"not found")
            return
        t=self.start
        while t is not None:
            if t.item==key:
                break
            t=t.next
        if t is None:
            print(key,"not found")
        else:
            newnode=Node(x)
            newnode.next=t.next
            t.next=newnode """

""" # 8. In class SLL, define a method to print all the elements of the list.
    def print_list(self):
        t=self.start
        while t is not None:
            print(t.item,end=' ')
            t=t.next """

# 9. In class SLL, implement iterator for SLL to access all the elements of the list in a sequence.

""" # 10. In class SLL, define a method delete_first() to delete first element from the list.
    def delete_first(self):
        if self.is_empty():
            print("List is Empty")
            return
        self.start=self.start.next """

""" # 11. In class SLL, define a method delete_last() to delete last element from the list.
    def delete_last(self):
        if self.is_empty():
            print("List is Empty")
            return
        if self.start.next is None:
            self.start=None
        else:
            t=self.start
            while t.next.next is not None:
                t=t.next
            t.next=None """

""" # 12. In class SLL, define a method delete_item() to delete specified element from the list.
    def delete_Item(self,x):
        if self.search(x):
            if self.start.item==x:
                self.delete_first()
            else:
                t=self.start
                while t.next is not None and t.next.item != x:
                    t=t.next
                t.next=t.next.next """