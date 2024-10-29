'''
Name:ganga
date:29-10-2024
python program to count vowels in a string
'''

string=input("enter string")
consonant_count=0
vowel_count=0
for char in string:
    if char in 'aeiouAEIOU':
        vowel_count+=1
    else:
        consonant_count+=1
print(f"The number of vowels in given string is {vowel_count} ")
print(f"The number of consonants in given string is {consonant_count} ")
