class Solution:
    def arraySign(self, nums: list[int]) -> int:
        neg = 0
        for n in nums:
            if n == 0:
                return 0
            neg += (1 if n < 0 else 0)

        return -1 if neg % 2 else 1

solution = Solution()
nums_positive = [2, 3, 4]
result_positive = solution.arraySign(nums_positive)
print(result_positive)  # Output: 1 (omdat het aantal negatieve getallen even is)

nums_mixed = [-1, -2, -3, 4]
result_mixed = solution.arraySign(nums_mixed)
print(result_mixed)  # Output: -1 (omdat het aantal negatieve getallen oneven is)

nums_zero = [0, 5, 7]
result_zero = solution.arraySign(nums_zero)
print(result_zero)  # Output: 0 (omdat er een nul in de lijst is)