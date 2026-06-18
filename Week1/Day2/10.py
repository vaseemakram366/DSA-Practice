# Store Discount Calculation



# amount = 6000

# if amount > 5000:
#     discount = amount * 0.20
#     final_amount = amount - discount
#     print("Final Amount =", final_amount)
# else:
#     print("Final Amount =", amount)

amount = float(input("Enter purchase amount: "))

if amount > 5000:
    final_amount = amount - (amount * 0.20)
else:
    final_amount = amount

print("Final Amount =", final_amount)