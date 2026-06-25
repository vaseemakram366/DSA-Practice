# Question 1: Print All Elements Row-Wise

n = int(input("Enter number of rows: "))
m = int(input("Enter number of columns: "))

arr = []

for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

print("Elements row-wise:")

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=" ")
    print()