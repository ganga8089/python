'''
name=ganga
date:15/10/2024
version:1.1
python program to determine the entry ticket fare in a zoo based on age
'''
age=int(input("Enter your age"))
if age<10:
    print("fare=7")
elif age>=10 and age<60:
    print("fare=10")
else:
    print("fare=5")