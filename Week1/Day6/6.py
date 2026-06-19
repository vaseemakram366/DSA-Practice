# Question 6:
# Given an array of integers, print only the odd numbers.

# arr = [10, 21, 30, 43, 50]

# for num in arr:
#     if num % 2 != 0:
#         print(num)


# OR

n = int(input())

arr = []

for i in range(n):
    arr.append(int(input()))

for num in arr:
    if num % 2 != 0:
        print(num)
