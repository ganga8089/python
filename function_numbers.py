'''
name:ganga
date:30-11-2024
version1.1
Program to check whether the given number is a valid mobile number or not using functions.
'''
def check_mobile_number(number):
        if len(number)==10 and number[0] in '789':
            print("The given is a valid mobile number")
        else:
            print("The given mobile number is not valid")
number=input("Enter mobile number:")
check_mobile_number(number)