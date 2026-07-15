#1st Approach: Recursively, Backtracking
# Time:
# Space:

#2nd Approach:
# Time:
# Space:

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []

        #base case
        if (len(nums) == 1):
            return [nums.copy()]

        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)
            result.extend(perms)
            nums.append(n)

        return result

# Voorbeeld
solution = Solution()
result = solution.permute([1, 2, 3])
print("Permutaties:", result)