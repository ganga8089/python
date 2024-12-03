'''
name:ganga
date:30-11-2024
version1.1
To print addition of two numbers using recursion
'''
def sum_numbers(num1,num2):
    if num2==0:
        return num1
    else:
        return sum_numbers(num1+1,num2-1)
num1=int(input("Enter number:"))
num2=int(input("enter number:"))
result=sum_numbers(num1,num2)
print("Sum=",result)