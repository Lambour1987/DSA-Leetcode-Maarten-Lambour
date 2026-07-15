#1st Approach:
# Time: O(n)
# Space: O(1)

#skip
#keep track of consequtive zeros
#shift pointer
#count
#reset count


from typing import List

class Solution:
    def zeroFieldSubarray(self, nums: List[int]) -> int:
        i, res = 0, 0

        while i < len(nums):
            count = 0

            # Zoek naar opeenvolgende nullen
            while i < len(nums) and nums[i] == 0:
                count += 1
                i += 1
                res += count

            i += 1

        return res

# Voorbeeldgebruik:
nums_example = [0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0]
solution_instance = Solution()
result = solution_instance.zeroFieldSubarray(nums_example)
print(f"Het totale aantal nullen in opeenvolgende deelarrays is: {result}")

