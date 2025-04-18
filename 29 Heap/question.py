# Assignment-29: Heap

""" # 1. Define a class Heap to implement Heap data structure with _init_method to create empty heap list.
class Heap:
    def __init__(self):
        self.heap = [] """

""" # 2. In class Heap, define a method to create heap from a given list of elements.

    def create_heap(self,data_list):
        for e in data_list:
            self.insert(e) """

""" # 3. In class Heap, define a method insert to insert a given element in the heap at appropriate position.
    def insert(self, data):
        self.heap.append(data)
        index = len(self.heap) - 1
        parent_index = (index - 1) // 2

        while index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = (index - 1) // 2 """

""" # 4. In class Heap, define a top method which returns the top element of the Heap. Raise an exception if Heap is empty.
    def top(self):
        if len(self.heap)==0:
            raise EmptyHeapException()
        else:
            return self.heap[0] """

""" # 5. Define a class Empty HeapException to describe custom exception.
class EmptyHeapException(Exception):
    def __init__(self,msg="Heap is empty"):
        self.msg=msg

    def __str__(self):
        return self.msg """

""" # 6. In class Heap, define a method delete which deletes the top element and returns it. Raise an exception if Heap is empty.
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
        
        return max_value """

""" # 7. In class Heap, define a method heapSort to sort a given list with the help of Heap.
    def heapsort(self, list1):
        self.create_heap(list1)
        sorted_list = []
        while len(self.heap) > 0:
            sorted_list.append(self.delete())
        return sorted_list[::-1] """