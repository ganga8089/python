'''
name=ganga
date:15/10/2024
version:1.1
python program to determine smallest of three numbers
'''
n1=int(input("Emter first number:"))
n2=int(input("Emter second number:"))
n3=int(input("Emter third number:"))
if n1<n2 and n1<n3:
    print(n1,"is smallest")
elif n2<n1 and n2<n3:
    print(n2,"is smallest")
else:
    print(n3,"is smallest")