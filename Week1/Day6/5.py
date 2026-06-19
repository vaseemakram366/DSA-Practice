# Question 5:
# Given an array of integers, count how many even numbers are present.

# arr = [10, 21, 30, 43, 50]

# count = 0

# for num in arr:
#     if num % 2 == 0:
#         count += 1

# print("Even Count =", count)


# OR

n = int(input())

arr = []

for i in range(n):
    arr.append(int(input()))

count = 0

for num in arr:
    if num % 2 == 0:
        count += 1

print(count)