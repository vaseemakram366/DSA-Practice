# Given a list of integers, count how many times the largest element appears.

nums = [10, 40, 25, 40, 8, 40]

largest = nums[0]

for num in nums:
    if num > largest:
        largest = num

count = 0

for num in nums:
    if num == largest:
        count += 1

print("Largest element:", largest)
print("Count:", count)