class Node:
    def __init__(self,item=None,priority=None,next=None):
        self.item=item
        self.priority=priority
        self.next=next

class PriorityQueue:
    def __init__(self,start=None):
        self.start=start
        self.item_count=0

    def is_empty(self):
        return self.start==None
    
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
        self.item_count += 1
            
    def pop(self):
        if self.is_empty():
            raise IndexError("Priority Queue is Underflow")
        else:
            data=self.start.item
            self.start=self.start.next
            self.item_count-=1
            return data

    def size(self):
        return self.item_count
    
    def print_item(self):  
        t=self.start
        while t is not None:
            print(t.item,end=' ')
            t=t.next
        print() 

p=PriorityQueue()
p.push("Arun",5)
p.push("Amit",8)
p.push("Anuj",3)
p.print_item()