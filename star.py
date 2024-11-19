'''
name:ganga
date:19-11-2024
version1.1
Program to construct patterns of stars (*), using a nested for loop.
'''
rows=int(input("Enter number of rows:"))
for i in range(rows):
    for j in range(i+1):
        print("*",end=" ")
    print( )
print( )
for i in range(rows-1,-1,-1):
    for j in range(i+1):
        print("*",end=" ")
    print( )
print( )
for i in range(1,rows+1):
    for k in range(rows-i):
        print(' ',end=" ")
    for j in range((2*i)-1):
        print('*',end=" ")
    print( )
print( )
for i in range(rows,-1,-1):
    for k in range(rows-i):
        print(' ',end=" ")
    for j in range((2*i)-1):
        print('*',end=" ")
    print( )
