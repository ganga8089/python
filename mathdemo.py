'''
name:ganga
version:1.1
date:05/10/2024
Write a Python program that uses functions from the math module to perform the following operations on a number provided by the user:

    Find the square root.
    Calculate the factorial.
    Raise the number to the power of 2.
'''
import math
number=int(input("Enter number:"))
print("square root of",number, ":",math.sqrt(number))
print("factorial of",number,":",math.factorial(number))
print(number,"raised to power 2:",math.pow(number,2))