'''
name:ganga
date:30-11-2024
version1.1
function that checks if a given string is a palindrome
'''
def is_palindrome(string):
    if string==string[::-1]:
        print(f"The given string is palindrome!!")
    else:
        print(f"The given string is not palindrome!!")
string=input("Enter string:")
is_palindrome(string)

