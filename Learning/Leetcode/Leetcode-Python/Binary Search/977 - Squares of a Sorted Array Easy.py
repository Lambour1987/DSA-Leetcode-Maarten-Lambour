#1st Approach:
# Time:
# Space:

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        res = []

        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l]  * nums[l] > nums[r] * nums[r]:
                res.append(nums[l] * nums[l])
                l += 1
            else:
                res.append(nums[r] * nums[r])
                r -= 1

        return res[::-1] # reverse

# Maak een instantie van Solution
solution = Solution()

# Voorbeeld
nums = [-4, -1, 0, 3, 10]
result = solution.sortedSquares(nums)

# Controleer het resultaat
print("Oorspronkelijke array:", nums)
print("Gesorteerde kwadraten array:", result)