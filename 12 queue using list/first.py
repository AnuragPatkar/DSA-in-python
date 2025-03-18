class Queue:
    def __init__(self):
        self.t=[]

    def is_empty(self):
        return len(self.t)==0
    
    def enqueue(self,data):
        self.t.append(data)
        
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        else:
            self.t.pop(0)
        
    def getFront(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        else:
            return self.t[0]
        
    def getRear(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        else:
            return self.t[-1]

    def size(self):
        return len(self.t)


q1=Queue()
print(q1.is_empty())
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
print(q1.getFront())
print(q1.getRear())
q1.dequeue()
print(q1.getFront())
print(q1.size())