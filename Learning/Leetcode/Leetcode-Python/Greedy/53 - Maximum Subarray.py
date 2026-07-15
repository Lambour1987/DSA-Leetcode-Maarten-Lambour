#1st Approach: Cubic Solution
# Time:
# Space:

#2nd Approach: Quadratic Solution
# Time:
# Space:

#3nd Approach: Lineair Solution
# Time:
# Space:

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxSub = nums[0]
        curSum = 0

        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)
        return maxSub

solution = Solution()

# Voorbeeld
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = solution.maxSubArray(nums)
print(result)  # Output: 6 (de maximale deelreeks is [4, -1, 2, 1])