# 268. Missing Number

# Method 1: Sum Formula

class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)

# Time Complexity: O(n)
# Space Complexity: O(1)

# Method 2: XOR

class Solution:
    def missingNumber(self, nums):
        ans = len(nums)

        for i, num in enumerate(nums):
            ans ^= i ^ num

        return ans

# Time Complexity: O(n)
# Space Complexity: O(1)