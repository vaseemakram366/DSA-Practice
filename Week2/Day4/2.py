# Question 2: Sum of Elements in Each Row

n = int(input("Enter number of rows: "))
m = int(input("Enter number of columns: "))

arr = []

for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

print("Row sums:")

for i in range(n):
    row_sum = 0

    for j in range(m):
        row_sum += arr[i][j]

    print(f"Row {i}: {row_sum}")