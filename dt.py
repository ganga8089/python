'''
AUTHOR: ganga
PROGRAM:ARITHMETIC OPERATIONS
DATE:08-10-2024
VERSION 1.1
'''
from datetime import datetime
current_time=(datetime.now())
print(current_time)
format1=current_time.strftime("%Y-%m-%d %H:%M:%S")
print(format1)
format2=current_time.strftime("%m/%d/%Y")
print(format2)
format3=current_time.strftime("%A,%B %d,%Y")
print(format3)
format4=current_time.strftime("%A,%B %d,%Y %H:%M:%S %p")
print(format4)
format5=current_time.strftime("%a-%b-%d %H:%M:%S IST %Y")
print(format5)
format6=current_time.strftime("%a-%b-%d %H:%M:%S IST %Y")
print(format6)
print(current_time.isoformat())
format7=current_time.strftime("%Y-%m_%d")
print(format7)
format8=current_time.strftime("%H:%M:%S")
print(format8)
format9=current_time.strftime("%B")
print(format9)
format10=current_time.strftime("%Y")
print(format10)