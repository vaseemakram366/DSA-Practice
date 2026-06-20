# Given a list of integers, find the difference between the sum of even numbers and the sum of odd numbers.

nums = [1, 2, 3, 4, 5, 6]

even_sum = 0
odd_sum = 0

for num in nums:
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

difference = even_sum - odd_sum

print("Sum of even numbers =", even_sum)
print("Sum of odd numbers =", odd_sum)
print("Difference =", difference)