#1st Approach: Backtracking, DFS
# Time:
# Space:

#2nd Approach:
# Time:
# Space:

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []

        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            #decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # decision NOT to include nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res

solution = Solution()

# Voorbeeld
nums = [1, 2, 3]
result = solution.subsets(nums)
print("Alle subsets:", result)