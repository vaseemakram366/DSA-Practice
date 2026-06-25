# Question 3: Search a Key in a 2D Array

n = int(input("Enter number of rows: "))
m = int(input("Enter number of columns: "))

arr = []

for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

key = int(input("Enter key to search: "))

found = False

for i in range(n):
    for j in range(m):
        if arr[i][j] == key:
            print("Key found at position:")
            print(f"({i}, {j})")
            found = True
            break

    if found:
        break

if not found:
    print("Key not found")