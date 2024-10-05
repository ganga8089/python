'''
name:ganga
version:1.1
date:05/10/2024
Write a Python program that demonstrates the usage of arithmetic, comparison, and logical operators. Perform a few operations and print the results.

'''
a=int(input("Enter first number:"))
b=int(input("Enter second number"))
sum=a+b
print("Sum:",sum)
division=a/b
print("Division:",division)
print("Is ",a,"greater than ",b,"?",a>b)
print("Are ",a,"and",b,"equal?",a==b)
print("logical AND:",a>b and b<a)
print("logical OR:",a>b or b>a)