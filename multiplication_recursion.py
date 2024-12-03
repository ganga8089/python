'''
name:ganga
date:30-11-2024
version1.1
To print multiplication using recursion
'''
def multiplication(num1,num2):
    if num2==1:
        return num1
    else:
        return num1 + multiplication(num1,num2-1)
num1=int(input("Enter number:"))
num2=int(input("Enter number:"))
result=multiplication(num1,num2)
print("Multiplication=",result)