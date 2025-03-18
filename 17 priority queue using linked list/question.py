# Assignment-17: Priority queue using linked list

""" # 1. Define a Node class with instance member variables item, priority and next.
class Node:
    def __init__(self,item=None,priority=None,next=None):
        self.item=item
        self.priority=priority
        self.next=next """

""" # 2. Define a class PriorityQueue to implement priority queue data structure using singly linked list. Provide _init_() method to create a start reference variable (initially containing None) and item_count variable (initially 0).
class PriorityQueue:
    def __init__(self,start=None):
        self.start=start
        self.item_count=0 """

""" # 3. Define a push method in PriorityQueue class to insert new data with given priority.
    def push(self, data, priority):
        newnode = Node(data, priority)
        if self.is_empty() or self.start.priority > priority:
            newnode.next = self.start
            self.start = newnode
        else:
            t = self.start
            while t.next is not None and t.next.priority <= priority:
                t = t.next
            newnode.next = t.next
            t.next = newnode
        self.item_count += 1 """

""" # 4. Define a pop method in PriorityQueue class, which returns the highest priority data stored in the priority queue data structure. Raise exception if priority queue is empty.
    def pop(self):
        if self.is_empty():
            raise IndexError("Priority Queue is Underflow")
        else:
            data=self.start.item
            self.start=self.start.next
            self.item_count-=1
            return data """

""" # 5. Define is_empty method in PriorityQueue class to check if the priority queue is empty.
    def is_empty(self):
        return self.start==None """

""" # 6. In class PriorityQueue, define a method size to return the number of elements present in the priority queue.
    def size(self):
        return self.item_count """