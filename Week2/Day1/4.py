# 1295. Find Numbers with Even Number of Digits

# Method 1: Convert to String

class Solution:
    def findNumbers(self, nums):
        count = 0

        for num in nums:
            if len(str(num)) % 2 == 0:
                count += 1

        return count

# Time Complexity: O(n)
# Space Complexity: O(1)

# Method 2: Mathematical Approach

class Solution:
    def findNumbers(self, nums):
        count = 0

        for num in nums:
            digits = 0
            while num > 0:
                digits += 1
                num //= 10

            if digits % 2 == 0:
                count += 1

        return count

# Time Complexity: O(n log n)**
# Space Complexity: O(1)