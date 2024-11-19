'''
name:ganga
date:19-11-2024
version1.1
Input two lists from the user. Merge these lists into a third list such that in the merged list, all even numbers occur first followed by odd numbers. Both the even numbers and odd numbers should be in sorted order.
'''
list_1=[]
number_element1=int(input("Enter the number of elements in list1:"))
for i in range(number_element1):
    number=int(input("Enter element:"))
    list_1.append(number)
list_2=[]
number_element2=int(input("Enter the number of elements in list2:"))
for i in range(number_element2):
    number=int(input("Enter number:"))
    list_2.append(number)
print("List1=",list_1)
print("list2=",list_2)
list=list_1+list_2
print("combined list=",list)
even_list=[]
odd_list=[]
for i in list:
    if i %2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
even_list.sort()
odd_list.sort()
my_list=even_list + odd_list
print("List=",my_list)