class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        res = len(nums)

        for i in range(len(nums)):
            res += (i - nums[i]) #betekent dus res = res + (i-nums[i])
        return res

solution = Solution()

# Voorbeeld
nums = [3, 0, 1]
result = solution.missingNumber(nums)
print(result)  # Output: 2 (Het ontbrekende getal tussen 0 en 3 is 2)