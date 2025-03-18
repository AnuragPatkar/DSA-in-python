# Assignment-18: Simple problems on recursion

""" # 1. Write a recursive function to print first N natural numbers.
def print_natural_numbers(n):
    if n==0:
        return
    print_natural_numbers(n-1)
    print(n)

x=int(input("Enter a number:"))
print_natural_numbers(x)  """

""" # 2. Write a recursive function to print first N natural numbers in reverse order.
def print_reverse_natural_numbers(n):
    print(n)
    if n==0:
        return
    print_reverse_natural_numbers(n-1)

x=int(input("Enter a number:"))
print_reverse_natural_numbers(x) """

""" # 3. Write a recursive function to print first N odd natural numbers.
def print_odd_natural_numbers(n):
    if n==0:
        return
    print_odd_natural_numbers(n-1)
    print(2*n-1)

x=int(input("Enter a number:"))
print_odd_natural_numbers(x) """

""" # 4. Write a recursive function to print first N even natural numbers
def print_even_natural_numbers(n):
    if n==0:
        return
    print_even_natural_numbers(n-1)
    print(2*n)

x=int(input("Enter a number:"))
print_even_natural_numbers(x) """

""" # 5. Write a recursive function to print first N odd natural numbers in reverse order.
def print_reverse_odd_natural_numbers(n):
    print(2*n-1)
    if n==0:
        return
    print_reverse_odd_natural_numbers(n-1)

x=int(input("Enter a number:"))
print_reverse_odd_natural_numbers(x) """

""" # 6. Write a recursive function to print first N even natural numbers in reverse order
def print_reverse_even_natural_numbers(n):
    print(2*n)
    if n==0:
        return
    print_reverse_even_natural_numbers(n-1)

x=int(input("Enter a number:"))
print_reverse_even_natural_numbers(x) """