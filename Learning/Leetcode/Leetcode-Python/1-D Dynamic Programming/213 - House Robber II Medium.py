#1st Approach:
# Time:
# Space:

class Solution:
    def rob(self, nums: list[int]) -> int:
        return max(nums[0] + self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        rob1, rob2 = 0, 0

        for n in nums:
            newRob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2

solution_instance = Solution()
nums = [2, 7, 9, 3, 1]
result = solution_instance.rob(nums)
print(result)