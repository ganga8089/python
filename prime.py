'''
name:ganga
date:12-11-2024
python program to check whether given number is prime or not
'''
n=int(input("Enter a number:"))
for num in range(2,n):
    if n%num==0:
        print(f"The given number {n} is not a prime number")
        break
else:
    print(f"The given number {n} is prime")
