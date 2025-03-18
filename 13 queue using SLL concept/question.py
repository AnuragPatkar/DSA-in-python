# Assignment-13: Queue using Singly Linked List Concept

""" # 1. Define a class Queue to implement queue data structure using singly linked list concept. Define _init_() method to initialise front and rear reference variable; and item_count variable to keep track of number of elements in the queue.
class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class Queue:
    def __init__(self,front=None,rear=None):
        self.front=front
        self.rear=rear
        self.item_count=0 """

""" # 2. Define a method is_empty() to check if the queue is empty in Queue class.
    def is_empty(self):
        return self.rear==None """

""" # 3. In Queue class, define enqueue() method to add data into the queue.
    def enqueue(self,data):
        newnode=Node(data)
        if self.is_empty():
            self.front=newnode
            self.rear=newnode
        else:
            self.rear.next=newnode
            self.rear=newnode
        self.item_count+=1 """

""" # 4. In Queue class, define dequeue() method to remove front element from the queue.
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        elif self.front==self.rear:
            self.rear=None
            self.front=None
            self.item_count-=1
        else:
            self.front=self.front.next
            self.item_count-=1 """

""" # 5. In Queue class, define get_front() method to return front element of the queue.
    def getFront(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        else:
            return self.front.item """

""" # 6. In Queue class, define get_rear() method to return rear element of the queue.
    def getRear(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        else:
            return self.rear.item """

""" # 7. In Queue class, define size() method to return size of the queue that is number of items present in the queue.
    def size(self):
        return self.item_count """