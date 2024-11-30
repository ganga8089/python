'''
name:ganga
date:30-11-2024
version1.1
python program to count upper cases and lower cases.
'''
def count(string):
    count_upper=0
    count_lower=0
    for character in string:
        if character.isupper():
            count_upper+=1
        else:
            count_lower+=1
    return count_upper,count_lower
string=input("enter string:")
upper_characters,lower_characters=count(string)
print("UPPER:",upper_characters)
print("LOWER:",lower_characters)
