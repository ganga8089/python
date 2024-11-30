'''
name:ganga
date:30-11-2024
version1.1
Python program to find sum of two numbers using function.
'''
def add_numbers(num_1,num_2):
    sum=num_1+num_2
    return sum
num1=int(input("Enter number:"))
num2=int(input("Enter number:"))
result=add_numbers(num1,num2)
print(f"Sum of {num1} and {num2} ={result}")