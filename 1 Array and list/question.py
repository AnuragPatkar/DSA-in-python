#Assignment-1: Array and list

""" #1. Given an array with some integer type values. Write a python script to sort array values?
from array import *
arr=array('i',[50,30,25,40,90,47])
sorted_arr=array('i',sorted(arr))
print(sorted_arr) """

""" from array import *
arr=array('i',[50,30,25,40,90,47])
arr_list=list(arr)
arr_list.sort()
arr=array('i',arr_list)
print(arr) """

""" arr=[10,25,30,15,18]
sorted_arr=sorted(arr)
print(sorted_arr) """

""" #2. Given a list of heterogenous elements. Write a python script to remove all the non int values from the list.
from array import *
l1=[1,2.2,"jabalpur","ABC",55]
filtered=[x for x in l1 if type(x)==int]
print(filtered) """

""" #3. Write a Python script to calculate average of elements of a list.
l1=[10,20,25,30,45,50]
s=0
for i in l1:
    s+=i
avr=s/len(l1)
print("Average:",avr)

average=sum(l1)/len(l1)
print("Average:",average) """

""" #4. Write a Python script to create a list of first N prime numbers.
def isprime(x):
     i=2
     while(i<x):
          if(x%i==0):
           break
          i+=1
     if x==i:
         return True
     else:
         return False
          
n=int(input("Enter a number:"))
l1=[]
i=2
while len(l1)<n :
    if isprime(i):
        l1.append(i)    
    i=i+1
print(l1) """

""" #5. Write a Python script to create a list of first N terms of a Fibonacci series
n=int(input("Enter a Number:"))
l1=[]
a=-1
b=1
c=a+b
while len(l1)<n:
    l1.append(c)
    a=b
    b=c
    c=a+b
print(l1) """
