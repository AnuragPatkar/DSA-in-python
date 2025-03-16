class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class SLL:
    def __init__(self, node=None):
        self.start = node

    def is_empty(self):
        return self.start is None

    def insert_at_start(self, x):
        new_node = Node(x)
        new_node.next = self.start
        self.start = new_node
    
    def insert_at_last(self, x):
        new_node = Node(x)
        if self.is_empty():
            self.start = new_node
        else:
            t = self.start
            while t.next is not None:
                t = t.next
            t.next = new_node
   
    def search(self,x):
        if self.is_empty():
            return False
        t=self.start
        while t is not None:
            if t.item == x:
                return True
            t=t.next
        return False
    
    def insert_after(self,key,x):
        if self.is_empty():
            print(key,"not found")
            return
        t=self.start
        while t is not None:
            if t.item==key:
                break
            t=t.next
        if t is None:
            print(key,"not found")
        else:
            newnode=Node(x)
            newnode.next=t.next
            t.next=newnode

    def print_list(self):
        t=self.start
        while t is not None:
            print(t.item,end=' ')
            t=t.next
        print()

    def delete_first(self):
        if self.is_empty():
            print("List is Empty")
            return
        self.start=self.start.next

    def delete_last(self):
        if self.is_empty():
            print("List is Empty")
            return
        if self.start.next is None:
            self.start=None
        else:
            t=self.start
            while t.next.next is not None:
                t=t.next
            t.next=None
    
    def delete_Item(self,x):
        if self.search(x):
            if self.start.item==x:
                self.delete_first()
            else:
                t=self.start
                while t.next is not None and t.next.item != x:
                    t=t.next
                t.next=t.next.next

s1=SLL()
s1.insert_at_start(10) 
s1.insert_at_start(30) 
s1.insert_at_start(25) 
s1.insert_at_last(50)
s1.insert_at_last(40)
s1.insert_after(50,100)
s1.print_list()
print(s1.search(60))
print(s1.search(10))
print(s1.is_empty())
s1.delete_first()
s1.delete_last()
s1.delete_Item(100)
s1.print_list()


        