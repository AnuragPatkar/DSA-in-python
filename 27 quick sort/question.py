#Assignment-27: Quick Sort

#!1. Write a python function to implement quick sort
def Quick_sort(list1,left,right):
    if left<right:
        m=Quick_process(list1,left,right)
        Quick_sort(list1,left,m-1)
        Quick_sort(list1,m+1,right)

def Quick_process(list1,left,right):
    mid=left
    while True:
        if left==right:
            break
        while list1[mid]<list1[right]:
            right-=1
        if list1[mid]>list1[right]:
            list1[mid],list1[right]=list1[right],list1[mid]
            mid=right
        while list1[mid]>list1[left]:
            left+=1
        if list1[mid]<list1[left]:
            list1[mid],list1[left]=list1[left],list1[mid]
            mid=left
    return mid
    

list1=[50,55,30,45,40,32,52,60,99,75]
Quick_sort(list1,0,len(list1)-1)
print(list1)