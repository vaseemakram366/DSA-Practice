# Given a list of integers, find the index of the largest element.

nums = [10, 25, 8, 40, 15]

largest = nums[0]
index = 0

for i in range(len(nums)):
    if nums[i] > largest:
        largest = nums[i]
        index = i

print("Index of largest element:", index)