#1st Approach: Dynamic Programming, Cache, Bottum Up DP, Memoization
# Time: O(n*m)
# Space:

class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = {0 : 1} initiele waarde

        for total in range(1, target + 1):
            dp[total] = 0
            for n in nums:
                dp[total] += dp.get(total-n, 0)

        return dp[target]

# Voorbeeldgebruik
solution = Solution()

# Voorbeeld 1
nums1 = [1, 2, 3]
target1 = 4
result1 = solution.combinationSum4(nums1, target1)
print(result1)  # Output: 7

# Voorbeeld 2
nums2 = [9]
target2 = 3
result2 = solution.combinationSum4(nums2, target2)
print(result2)  # Output: 0