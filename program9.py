'''
name=ganga
date:15/10/2024
version:1.1
python program to determine larger of two numbers
'''
num1=int(input("Enter number 1:"))
num2=int(input("Enter number 2:"))
if num1>num2:
    print(num1,"is larger than",num2)
elif num1<num2:
    print(num2,"is larger than ",num1)
else:
    print("Both numbers are equal")