# 3. Find GCD/HCF of two numbers


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while b != 0:
    a, b = b, a % b

print("HCF =", a)