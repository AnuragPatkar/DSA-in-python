# Assignment-19: Simple problems on recursion

""" # 1. Write a recursive function to calculate sum of first N natural numbers.
def sum_of_natural_num(n):
    if n==0:
        return 0
    return n+ sum_of_natural_num(n-1)

x=int(input("Enter a number:"))
print(sum_of_natural_num(x)) """

""" # 2. Write a recursive function to calculate sum of first N odd natural numbers
def sum_of_odd_natural_num(n):
    if n==0:
        return 0
    return 2*n-1+ sum_of_odd_natural_num(n-1)

x=int(input("Enter a number:"))
print(sum_of_odd_natural_num(x)) """

""" # 3. Write a recursive function to calculate sum of first N even natural numbers
def sum_of_even_natural_num(n):
    if n==0:
        return 0
    return 2*n+ sum_of_even_natural_num(n-1)

x=int(input("Enter a number:"))
print(sum_of_even_natural_num(x)) """

""" # 4. Write a recursive function to calculate factorial of a number.
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)

x=int(input("Enter a number:"))
print(fact(x)) """

""" # 5. Write a recursive function to calculate sum of squares of first N natural numbers
def sum_of_squre_of_natural_num(n):
    if n==0:
        return 0
    return n**2+ sum_of_squre_of_natural_num(n-1)

x=int(input("Enter a number:"))
print(sum_of_squre_of_natural_num(x)) """