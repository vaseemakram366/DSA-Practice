# Question 9:
# Given an array of integers, print the elements in reverse order.

# arr = [10, 20, 30, 40, 50]

# for i in range(len(arr) - 1, -1, -1):
#     print(arr[i])


# OR

n = int(input())

arr = []

for i in range(n):
    arr.append(int(input()))

for i in range(n - 1, -1, -1):
    print(arr[i])