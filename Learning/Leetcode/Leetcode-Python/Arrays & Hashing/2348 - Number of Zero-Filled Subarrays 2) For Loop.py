#1st Approach:
# Time: O(n)
# Space: O(1)

#skip
#keep track of consequtive zeros
#shift pointer
#count
#reset count

class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
       res, count = 0, 0

       for i in range(len(nums)):
           if nums[i] == 0:
               count += 1
           else:
               count = 0
           res += count #res = res + count
       return res

# Voorbeeldgebruik:
# Voorbeeldgebruik:
nums_example = [0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0]
solution_instance = Solution()
result = solution_instance.zeroFilledSubarray(nums_example)
print(f"Het totale aantal nullen in opeenvolgende deelarrays is: {result}")