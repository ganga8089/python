'''
name:ganga
date:30-11-2024
version1.1
To find GCD of two numbers using recursion
'''
def gcd(num1,num2):
    if num1%num2==0:
        return num2
    else:
        return gcd(num2,num1%num2)
num1=int(input("Enter number:"))
num2=int(input("Enter number:"))
result=gcd(num1,num2)
print("GCD=",result)