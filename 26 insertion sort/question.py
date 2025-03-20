#Assignment-26: Insertion Sort

#!1. Write a python function to implement Insertion sort
def insertion_sort(list1):
    n=len(list1)
    for i in range(1, n):
        temp = list1[i]
        j = i - 1
        while j >= 0 and temp < list1[j]:
            list1[j + 1] = list1[j]
            j -= 1
        list1[j + 1] = temp

list1 = [55, 20, 35, 60, 25]
insertion_sort(list1)
print(list1)