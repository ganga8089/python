'''
name:ganga
date:17-12-2024
version1.1
To print power of two positive numbers using recursion
'''
def power(num1,num2):
    if num2==1:
        return num1
    else:
        return num1 * power(num1,num2-1)
num1=int(input("Enter number:"))
num2=int(input("Enter number:"))
result=power(num1,num2)
print(result)