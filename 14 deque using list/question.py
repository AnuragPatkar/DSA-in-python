# Assignment-14: Deque Implementation using list

""" # 1. Define a class Deque to implement deque data structure using list. Define init() method to create an empty list object as instance object member of Deque.
class deque:
    def __init__(self):
        self.mylist=[] """

""" # 2. Define a method is_empty() to check if the deque is empty in Deque class.
    def is_empty(self):
        return len(self.mylist)==0 """

""" # 3. In Deque class, define insert_front() method to add data at the front end of the deque.
    def insert_front(self,data):
        self.mylist.insert(0,data) """

""" # 4. In Deque class, define insert_rear() method to add data at the rear end of the deque.
    def insert_rear(self,data):
        self.mylist.append(data) """

""" # 5. In Deque class, define delete_front() method to remove front element from the deque.
    def delete_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        else:
            self.mylist.pop(0) """

""" # 6. In Deque class, define delete_rear() method to remove rear element from the deque.
    def delete_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        else:
            self.mylist.pop(-1) """

""" # 7. In Deque class, define get_front() method to return front element of the deque.
    def get_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        else:
            return self.mylist[0] """

""" # 8. In Deque class, define get_rear() method to return rear element of the deque.
    def get_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        else:
            return self.mylist[-1] """

""" # 9. In Deque class, define size() method to return size of the deque that is number of items present in the deque
    def size(self):
        return len(self.mylist) """