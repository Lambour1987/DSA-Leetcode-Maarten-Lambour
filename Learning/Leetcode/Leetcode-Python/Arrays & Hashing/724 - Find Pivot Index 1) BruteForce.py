#2st Approach:
# Time:
# Space:

from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0

        for i in range(len(nums)):
            right_sum = total - nums[i] - left_sum
            if left_sum == right_sum:
                return i
            left_sum += nums[i]

        return -1

# Voorbeeldgebruik:
example = Solution()
nums = [1, 7, 3, 6, 5, 6]
result = example.pivotIndex(nums)
print(result)