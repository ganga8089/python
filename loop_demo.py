'''
Name:Ganga
date:29-10-2028
version:1.1
python program to check whether given number is prime or not '''
number=int(input("enter a number"))
i=0
isPrime=True
for i in range(2,(number//2)+1):
    if number % i==0:
        isPrime=False
        break
if isPrime:
    print(f"The given number {number} is prime")
else:
    print(f"The given number {number} is not prime")
