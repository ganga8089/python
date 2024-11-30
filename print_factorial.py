'''
name:ganga
date:30-11-2024
version1.1
function that returns the factorial of a number.
'''
def factorial(number):
    factorial=1
    for i in range(1,number+1):
        factorial*=i
    return factorial
number=int(input("Enter number:"))
result=factorial(number)
print(f"Factorial of given number {number} is {result}")