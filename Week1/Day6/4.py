# Question 4:
# Given an array of integers, find and print the smallest element.

# arr = [10, 20, 30, 40, 50]

# smallest = arr[0]

# for num in arr:
#     if num < smallest:
#         smallest = num

# print("Smallest =", smallest)

# OR

n = int(input())

arr = []

for i in range(n):
    arr.append(int(input()))

smallest = arr[0]

for num in arr:
    if num < smallest:
        smallest = num

print(smallest)