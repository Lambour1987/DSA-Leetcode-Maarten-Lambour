#1st Approach:
# Time:
# Space:

class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        nums.sort()
        res = []

        l, r = 0, len(nums) - 1
        while len(res) != len(nums):
            res.append(nums[l])
            l += 1

            if l <= r:
                res.append(nums[r])
                r -= 1
        return res

# Voorbeeldgebruik
solution = Solution()
nums_example = [1, 2, 3, 4, 5]
result = solution.rearrangeArray(nums_example)
print(result)