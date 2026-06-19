# Given an array of integers, find and print the sum of all elements.

# arr = [10, 20, 30, 40, 50]

# total = 0

# for num in arr:
#     total += num

# print("Sum =", total)

# OR


n = int(input("Enter size of array: "))

arr = []

for i in range(n):
    arr.append(int(input()))

total = 0

for num in arr:
    total += num

print(total)