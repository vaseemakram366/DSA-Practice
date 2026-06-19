# Question 3:
# Given an array of integers, find and print the largest element.

# arr = [10, 20, 30, 40, 50]

# largest = arr[0]

# for num in arr:
#     if num > largest:
#         largest = num

# print("Largest =", largest)


# OR

n = int(input())

arr = []

for i in range(n):
    arr.append(int(input()))

largest = arr[0]

for num in arr:
    if num > largest:
        largest = num

print(largest)