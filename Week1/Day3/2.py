balance = float(input("Enter account balance: "))
withdraw = float(input("Enter withdrawal amount: "))

if withdraw <= balance:
    print("Withdrawal successful")
else:
    print("Insufficient balance")