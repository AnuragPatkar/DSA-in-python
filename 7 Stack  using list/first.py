class Stack:
    def __init__(self):
        self.t = []
    
    def is_empty(self):
        return len(self.t) == 0
    
    def push(self, data):
        self.t.append(data)

    def pop(self):
        if not self.is_empty():
            return self.t.pop()
        else:
            return None

    def peek(self):
        if self.is_empty():
            return "List is empty"
        else:
            return self.t[-1]

    def size(self):
        return len(self.t)

s1 = Stack()
print(s1.is_empty())
s1.push(30)
s1.push(20)
s1.push(10)
print(s1.is_empty())
print(s1.size())
print(s1.peek())
s1.pop()
print(s1.peek())