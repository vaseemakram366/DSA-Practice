# Given a list of integers, check if the list is sorted in ascending order.

nums = [1, 2, 3, 4, 5]

is_sorted = True

for i in range(len(nums) - 1):
    if nums[i] > nums[i + 1]:
        is_sorted = False
        break

if is_sorted:
    print("List is sorted in ascending order")
else:
    print("List is not sorted in ascending order")