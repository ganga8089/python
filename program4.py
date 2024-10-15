'''
name=ganga
date:15/10/2024
version:1.1
python program to calculate final amount after applying discount.
'''
purchase_amount=int(input("Enter the purchase amount:"))
if purchase_amount>500:
    discount=purchase_amount*0.2
    final_amount=purchase_amount-discount
    print("Final amount after applying 20% discount is",final_amount)
elif purchase_amount>=200 and purchase_amount<=500:
    discount=purchase_amount*0.1
    final_amount=purchase_amount-discount
    print("Final amount after applying 10% discount is",final_amount)
else:
    final_amount=purchase_amount
    print("No discount is applied.Final amount is",final_amount)