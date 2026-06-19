# Question 10:
# Given an array of integers, find the average of all elements.

# arr = [10, 20, 30, 40, 50]

# total = 0

# for num in arr:
#     total += num

# average = total / len(arr)

# print("Average =", average)


# OR

n = int(input())

arr = []

for i in range(n):
    arr.append(int(input()))

total = 0

for num in arr:
    total += num

average = total / n

print(average)