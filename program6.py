'''
name=ganga
date:15/10/2024
version:1.1
python program to print sum of digits
'''
number=int(input("Enter number:"))
sum=0
while(number>0):
    rem=number%10
    number=number//10
    sum=sum+rem
print("Sum of the digits=",sum)