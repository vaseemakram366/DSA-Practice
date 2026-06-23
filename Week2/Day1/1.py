# 2733. Neither Minimum nor Maximum


class Solution:
    def findNonMinOrMax(self, nums):
        if len(nums) < 3:
            return -1

        a, b, c = nums[0], nums[1], nums[2]
        return sorted([a, b, c])[1]


# Time Complexity: O(1)
# Space Complexity: O(1)