'''
name:ganga
date:12-11-2024
python program to print fibonacci number series
'''
limit=int(input("Enter a range:"))
first_number=1
second_number=0
third_number=0
while third_number<limit:
    print(third_number,end=" ")
    third_number=first_number+second_number
    first_number=second_number
    second_number=third_number
