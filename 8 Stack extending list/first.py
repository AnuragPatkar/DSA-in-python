class Stack(list):
    def push(self,item):
        self.append(item)
    
    def is_empty(self):
        return  len(self)==0
    
    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError("Stack is empty")
        
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("Stack is empty")
        
    def size(self):
        return len(self)
    
    def insert(self, index, data):
        raise AttributeError("NO insert function in Stack")
    
    
s1=Stack()
print(s1.is_empty())
s1.push(10)
s1.push(20)
s1.push(30)
print(s1.peek())
print(s1.pop())
print(s1.peek())
print(s1.size())
s1.insert(1,100)
print(s1.peek())