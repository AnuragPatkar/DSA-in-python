class Queue(list):
    def enqueue(self,data):
        self.append(data)

    def is_empty(self):
        return len(self)==0
    
    def dequeue(self):
        if self.is_empty():
           raise IndexError("Queue is empty")
        else:
           self.pop(0)

    def getFront(self):
        if self.is_empty():
           raise IndexError("Queue is empty")
        else:
           return self[0]
        
    def getRear(self):
        if self.is_empty():
           raise IndexError("Queue is empty")
        else:
           return self[-1]
        
    def size(self):
        return len(self)
    
q1=Queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
print(q1.getFront())
print(q1.getRear())
q1.dequeue()
print(q1.getFront())
print(q1.size())
