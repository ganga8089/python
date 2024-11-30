'''
name:ganga
date:30-11-2024
version1.1
function that takes a string and return it reversed.
'''
def reverse_string(string):
    reverse=string[::-1]
    return reverse
string = input("Enter string:")
reversed_string=reverse_string(string)
print("Reversed string:",reversed_string)
