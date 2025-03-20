# Assignment-25: Selection Sort

""" #! 1. Write a python function to implement selection sort
def selection_sort(l1):
    n=len(l1)
    for i in range(n-1):
        min_index=i
        for j in range(i+1,n):
            if l1[j]<l1[min_index]:
                min_index=j
        l1[i],l1[min_index]=l1[min_index],l1[i]
    


l1=[40,25,18,35,30]
selection_sort(l1)
print(l1) """