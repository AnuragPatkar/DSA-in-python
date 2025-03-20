# Assignment-24: Sorting

""" # 1. Write a python function to implement bubble sort
def Bubble_sort(l1):
    i=0
    j=0
    while i<len(l1)-1:
        while j<len(l1)-1-i:
            if l1[j]>l1[j+1]:
                temp=l1[j]
                l1[j]=l1[j+1]
                l1[j+1]=temp
            j+=1
        i+=1  """

""" def Bubble_sort(l1):  #for loop
    n=len(l1)
    for i in range(n-1):
        for j in range(n-1-i):
            if l1[j]>l1[j+1]:
                temp=l1[j]
                l1[j]=l1[j+1]
                l1[j+1]=temp
            
l1=[10,55,40,30,50]
Bubble_sort(l1)
print(l1) """

""" # 2. Write a python function to implement modified bubble sort.
def modified_Bubble_sort(l1):
    n=len(l1)
    for i in range(n-1):
        t=False
        for j in range(n-1-i):
            if l1[j]>l1[j+1]:
                temp=l1[j]
                l1[j]=l1[j+1]
                l1[j+1]=temp
                t=True
        if not t:
            break

            
l1=[10,55,40,30,50]
modified_Bubble_sort(l1)
print(l1) """