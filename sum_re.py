'''
name:ganga
date:17-12-2024
version1.1
To print sum of n numbers using recursion
'''
def sum_numbers(n):
    if n==0:
        return n
    else:
        return n + sum_numbers(n-1)
n=int(input("Enter number:"))
result=sum_numbers(n)
print(result)