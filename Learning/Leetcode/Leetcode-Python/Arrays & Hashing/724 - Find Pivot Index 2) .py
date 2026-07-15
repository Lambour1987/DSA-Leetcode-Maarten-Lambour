#1st Approach: BruteForce
# Time: O(n^2)
# Space:

class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total = sum(nums)
        leftSum = 0

        for i in range(len(nums)):
            rightSum = total - nums[i] - leftSum
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
        return -1

example = Solution()
nums = [1, 7, 3, 6, 5, 6]

result = example.pivotIndex(nums)
print(result)