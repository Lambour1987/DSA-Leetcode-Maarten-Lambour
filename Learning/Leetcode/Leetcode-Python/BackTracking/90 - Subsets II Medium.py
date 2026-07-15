class Solution:
    def subsetsWithDup(self, nums: List[int]) -> list[list[int]]:
        res = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                res.append