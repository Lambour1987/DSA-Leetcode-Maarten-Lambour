#1st Approach: BruteForce
# Time:
# Space:

#2nd Approach: Greedy
# Time:
# Space:

class Solution:
    def jump(self, nums: list[int]) -> int:
        res = 0
        l = r = 0

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res +=1
        return res

solution = Solution()

# Voorbeeld
nums = [2, 3, 1, 1, 4]
result = solution.jump(nums)
print(result)  # Output: 2