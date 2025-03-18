# Assignment-16: Priority queue using list

""" # 1. Define a class PriorityQueue to implement priority queue data structure using list. Provide_init__() method to create a list object (initially empty).
class PQ:
    def __init__(self):
        self.mylist=[] """

""" # 2. Define a push method in PriorityQueue class to insert new data with given priority.
    def push(self,data,priority):
        index=0
        while index < len(self.mylist) and self.mylist[index][1]<=priority:
            index += 1
        self.mylist.insert(index,(data,priority)) """

""" # 3. Define a pop method in Priority Queue class, which returns the highest priority data stored in the priority queue data structure. Raise exception if priority queue is empty.
    def pop(self):
        if self.is_empty():
            raise IndexError("Priority Queue is Underflow")
        else:
            return self.mylist.pop(0)[0] """

""" # 4. Define is_empty method in PriorityQueue class to check if the priority queue is empty.
    def is_empty(self):
        return len(self.mylist)==0 """

""" # 5. In class PriorityQueue, define a method size to return the number of elements present in the priority queue.
    def size(self):
        return len(self.mylist) """