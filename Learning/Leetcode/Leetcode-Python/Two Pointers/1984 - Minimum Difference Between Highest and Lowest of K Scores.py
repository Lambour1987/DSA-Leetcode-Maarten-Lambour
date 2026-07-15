#1st Approach: Sort & Sliding window
# Time: n(logn) vanwege sorting. Sliding window O(n). Overall Time nlog n
# Space:

#2nd Approach: (zelf: waarom sorteren? kan je ook met linker en rechter pointer en dan minimum zoeken? Of is dat BF
# Time:
# Space:

from typing import List

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, k-1
        res = float("inf")

        while r < len(nums):
            res = min(res, nums[r] - nums[l])
            l, r = l + 1, r + 1
        return res

solution = Solution()
nums = [1, 5, 3, 8, 10]
k = 2
result = solution.minimumDifference(nums, k)
print(result)