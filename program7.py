'''
name=ganga
date:15/10/2024
version:1.1
python program to check whether the given number is armstrong or not
'''
number=int(input("Enter a number:"))
armstrong=number
sum=0
while(number>0):
    rem=number%10
    number=number//10
    sum=sum=rem**3
if sum==armstrong:
    print("The given number is a armstrong number")
else:
    print("The given is not a armstrong number")