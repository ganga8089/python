'''name:ganga
date:19-11-2024
version:1.1
'''
list=[]
n=int(input("Enter number:"))
for i in range (n):
    number=int(input("Enter number:"))
    list.append(number)
print(list)
unique_list=[]
for number in list:
    if number not in unique_list:
        unique_list.append(number)
print(unique_list)
