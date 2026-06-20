# Given a list of integers, remove all occurrences of a given number and print the updated list.

nums = [1, 2, 3, 2, 4, 2, 5]
remove_num = 2

updated_list = []

for num in nums:
    if num != remove_num:
        updated_list.append(num)

print("Updated list:", updated_list)