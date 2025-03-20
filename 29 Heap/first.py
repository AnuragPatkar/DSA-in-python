class Heap:
    def __init__(self):
        self.heap = []

    def create_heap(self,data_list):
        for e in data_list:
            self.insert(e)

    def insert(self, data):
        self.heap.append(data)
        index = len(self.heap) - 1
        parent_index = (index - 1) // 2

        while index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = (index - 1) // 2
         
    def top(self):
        if len(self.heap)==0:
            raise EmptyHeapException()
        else:
            return self.heap[0]
        
    def delete(self):
        if len(self.heap) == 0:
            raise EmptyHeapException()
        if len(self.heap) == 1:
            return self.heap.pop()
        
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        
        index = 0
        leftchild = 2 * index + 1
        rightchild = 2 * index + 2
        
        while leftchild < len(self.heap):
            largest = index
            if leftchild < len(self.heap) and self.heap[leftchild] > self.heap[largest]:
                largest = leftchild
            if rightchild < len(self.heap) and self.heap[rightchild] > self.heap[largest]:
                largest = rightchild
            if largest == index:
                break
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            index = largest
            leftchild = 2 * index + 1
            rightchild = 2 * index + 2
        
        return max_value
    
    def heapsort(self, list1):
        self.create_heap(list1)
        sorted_list = []
        while len(self.heap) > 0:
            sorted_list.append(self.delete())
        return sorted_list[::-1]

class EmptyHeapException(Exception):
    def __init__(self,msg="Heap is empty"):
        self.msg=msg

    def __str__(self):
        return self.msg
    

l1=[10,55,42,61,78,16,48,85,25]
H=Heap()
l1=H.heapsort(l1)
print(l1)