# Question 8:
# Given an array of integers, create a new array containing the square
# of each element and print it.

# arr = [1, 2, 3, 4, 5]

# square_arr = []

# for num in arr:
#     square_arr.append(num ** 2)

# print(square_arr)


# OR

n = int(input())

arr = []

for i in range(n):
    arr.append(int(input()))

square_arr = []

for num in arr:
    square_arr.append(num * num)

print(square_arr)