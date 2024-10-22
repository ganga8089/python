'''
name:ganga
date:22/10/2024
python program to convert temperature to Celsius and Fahrenheit.
'''
temp=int(input("Enter temperature:"))
t=input("Is this in (C)elcius or (F)ahreheit?")
if t=='C':
    f=(9/5*temp)+32
    print(temp,"is",f,"fahrenheit")
else:
    c=5/9*(temp-32)
    print(temp,"is",c,"celcius")
