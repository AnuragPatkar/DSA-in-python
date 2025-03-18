# Assignment-12: Queue using list

""" # 1. Define a class Queue to implement queue data structure using list. Define _init__() method to create an empty list object as instance object member of Queue.
class Queue:
    def __init__(self):
        self.t=[] """

""" # 2. Define a method is_empty() to check if the queue is empty in Queue class.
    def is_empty(self):
        return len(self.t)==0 """

""" # 3. In Queue class, define enqueue() method to add data at the rear end of the queue.
    def enqueue(self,data):
        self.t.append(data) """

""" # 4. In Queue class, define dequeue() method to remove front element from the queue.
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        else:
            self.t.pop(0) """

""" # 5. In Queue class, define get_front() method to return front element of the queue.
    def getFront(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        else:
            return self.t[0] """

""" # 6. In Queue class, define get_rear() method to return rear element of the queue.
    def getRear(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        else:
            return self.t[-1] """

""" # 7. In Queue class, define size() method to return size of the queue that is number of items present in the queue.
    def size(self):
        return len(self.t) """