#2st Approach: Gebruik index als mapping
# Time: O(1)
# Space:

class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        # mark existing
        for n in nums:
            i = abs(n) - 1
            nums[i] = -1 * abs(nums[i])

        res = []
        for i, n in enumerate(nums, start=1):  # Begin bij 1, niet bij 0
            if n > 0:
                res.append(i)

        for i in range(len(nums)):
            nums[i] = abs(nums[i])

        return res

example = Solution()
nums = [4, 3, 2, 7, 8, 2, 1]

result = example.findDisappearedNumbers(nums)
print(result)