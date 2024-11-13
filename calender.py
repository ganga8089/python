'''
name:ganga
date:13-11-2024
Python Program to print calender for a given month and year.
'''
import calendar
year=int(input("Enter year"))
month=int(input("Enter month"))
print(calendar.month(year,month))