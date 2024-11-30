'''
name:ganga
date:30-11-2024
version1.1
function that takes a number and return True if it is even and False if it is odd.
'''
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
number=int(input("Enter number:"))
result=is_even(number)
print(result)