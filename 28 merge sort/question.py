# Assignment-28: Merge Sort

#! 1. Write a python function to implement Merge sort
def merge_sort(mylist):
    if len(mylist)>1:
        mid=len(mylist)//2
        leftlist=mylist[:mid]
        rightlist=mylist[mid:]
    
        merge_sort(leftlist)
        merge_sort(rightlist)

        i=j=k=0
        while i<len(leftlist) and j<len(rightlist):
            if leftlist[i]<rightlist[j]:
                mylist[k]=leftlist[i]
                i+=1
            else:

                mylist[k]=rightlist[j]
                j+=1
            k+=1

        while i<len(leftlist):
            mylist[k]=leftlist[i]
            i+=1
            k+=1

        while j<len(rightlist):
            mylist[k]=rightlist[j]
            j+=1
            k+=1

mylist=[55,30,45,60,80,65,75,25]
merge_sort(mylist)
print(mylist)
