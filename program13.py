'''
name=ganga
date:15/10/2024
version:1.1
python program to print n odd numbers
'''
limit=int(input("Enter the limit:"))
odd_number=1
count=0
while(count<limit):
    print(odd_number,"\t",end='')
    count+=1
    odd_number+=2
