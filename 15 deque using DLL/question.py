# Assignment-15: Deque using Doubly Linked List Concept

""" # 1. Define a class Node with instance object member variables prev, item and next.
class Node:
    def __init__(self,item=None,prev=None,next=None):
        self.item=item
        self.prev=prev
        self.next=next """

""" # 2. Define a class Deque to implement deque data structure using doubly linked list concept. Define _init_() method to initialise front and rear reference variable; and item_count variable to keep track of number of elements in the deque.
class Deque:
    def __init__(self,front=None,rear=None):
        self.front=front
        self.rear=rear
        self.item_count=0 """

""" # 3. Define a method is_empty() to check if the deque is empty in Deque class.
    def is_empty(self):
        return self.front is None """

""" # 4. In Deque class, define insert_front() method to add data at the front of the deque.
    def insert_front(self,data):
        newnode=Node(data)
        if self.is_empty():
            self.front=newnode
            self.rear=newnode
        else:
            self.front.prev=newnode
            newnode.next=self.front
            self.front=newnode
        self.item_count+=1 """

""" # 5. In Deque class, define insert_rear() method to add data at the rear of the deque.
    def insert_rear(self,data):
        newnode=Node(data)
        if self.is_empty():
            self.front=newnode
            self.rear=newnode
        else:
            self.rear.next=newnode
            newnode.prev=self.rear
            self.rear=newnode
        self.item_count+=1 """

""" # 6. In Deque class, define delete_front() method to remove front element from the deque.
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
            self.item_count-=1 """

""" # 7. In Deque class, define delete_rear() method to remove rear element from the deque.
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
            self.item_count-=1 """

""" # 8. In Deque class, define get_front() method to return front element of the deque.
    def get_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        else:
            return self.front.item """

""" # 9. In Deque class, define get_rear() method to return rear element of the deque.
    def get_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        else:
            return self.rear.item """

""" # 10. In Deque class, define size() method to return size of the deque that is number of items present in the deque.
    def size(self):
        return self.item_count """