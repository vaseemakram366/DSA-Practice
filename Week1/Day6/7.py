# Question 7:
# Given an array of integers, count how many elements are greater than 10.

# arr = [5, 12, 8, 25, 15, 3]

# count = 0

# for num in arr:
#     if num > 10:
#         count += 1

# print("Count =", count)


# OR

n = int(input())

arr = []

for i in range(n):
    arr.append(int(input()))

count = 0

for num in arr:
    if num > 10:
        count += 1

print(count)