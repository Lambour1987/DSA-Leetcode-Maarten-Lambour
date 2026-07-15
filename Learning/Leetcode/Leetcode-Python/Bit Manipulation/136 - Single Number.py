#1st Approach: Hashset: Iedere waarde die 2x voorkomt wordt toegevoegd(1x) en daarna verwijderd(1). Dus de hashset blijft over met de waarde die maar 1x voorkomt.
# Time: O(n)
# Space: O(n)

#2nd Approach: Bit manipulation
# Time:
# Space:

#3nd Approach:
# Time:
# Space:

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res = 0
        for n in nums:
            res = n ^ res
        return res

solution = Solution()

# Voorbeeld
nums = [2, 2, 1, 4, 1]
result = solution.singleNumber(nums)
print(result)  # Output: 4