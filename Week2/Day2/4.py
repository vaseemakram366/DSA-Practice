# 4. Swap two numbers without third variable
# Method 1

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a = a + b
b = a - b
a = a - b

print("a =", a)
print("b =", b)

# Method 2 (Pythonic Way)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a, b = b, a

print("a =", a)
print("b =", b)