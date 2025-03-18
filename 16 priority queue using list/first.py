class PQ:
    def __init__(self):
        self.mylist=[]
    
    def push(self,data,priority):
        index=0
        while index < len(self.mylist) and self.mylist[index][1]<=priority:
            index += 1
        self.mylist.insert(index,(data,priority))


    def pop(self):
        if self.is_empty():
            raise IndexError("Priority Queue is Underflow")
        else:
            return self.mylist.pop(0)[0]
       
    
    def is_empty(self):
        return len(self.mylist)==0
    
    def size(self):
        return len(self.mylist)

pq1=PQ()
pq1.push(10,1)
pq1.push(40,4)
pq1.push(30,3)
pq1.push(50,5)
print(pq1.pop())
print(pq1.size())
