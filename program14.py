'''
name=ganga
date:15/10/2024
version:1.1
python program to print up to n odd numbers
'''
limit=int(input("Enter the limit:"))
odd_number=1

while(odd_number<=limit):
    print(odd_number,"\t",end='')

    odd_number+=2
