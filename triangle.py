'''
name:ganga
date:30-11-2024
version1.1
A program that accepts the lengths of three sides of a triangle as inputs. The program should output whether or not the triangle is a right triangle (Recall from the Pythagorean Theorem that in a right triangle, the square of one side equals the sum of the squares of the other two sides). Implement using functions.

'''
def check_triangle(list):
    if list[2]**2==list[1]**2 + list[0]**2:
        print("The given sides are part of right triangle")
    else:
        print("The given sides are not part of right triangle")
list=[]
for i in range(3):
    side=int(input("Enter side:"))
    list.append(side)
list.sort()
check_triangle(list)
