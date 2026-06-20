# Given a list of integers and a key, check if the key exists in the array.

nums = [10, 20, 30, 40, 50]
key = 30

found = False

for num in nums:
    if num == key:
        found = True
        break

if found:
    print("Key exists in the array")
else:
    print("Key does not exist in the array")