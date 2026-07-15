#1st Approach:
# Time:
# Space:

class Solution:
    def rob(self, nums: list[int]) -> int:
        rob1, rob2 = 0, 0 #tijdelijke variabelen. Alleen de laatste huizen zijn van belang voor het bepalen van de maximale opbrengst

        #[rob1,rob2,n,n+1, ...]
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

solution_instance = Solution()
nums = [2, 7, 9, 3, 1]
result = solution_instance.rob(nums)
print(result)