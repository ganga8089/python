'''
name:ganga
date:30-11-2024
version1.1
print factorial using recursion
'''
def factorial(number):
    if number==1:
        return 1
    else:
        return number * factorial(number-1)
number=int(input("Enter a number:"))
result=factorial(number)
print("Factorial=",result)