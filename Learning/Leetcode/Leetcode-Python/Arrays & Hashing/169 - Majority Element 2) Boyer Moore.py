#2nd Approach: Boyer - Moore Algorithm
# Time: Lineair
# Space: O(1)

# Volgens mij is dit Bucket

from typing import List

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        res, count = 0, 0 #not max count because it will increase or decrease

        for n in nums:
            if count == 0:
                res = n
            count += (1 if n == res else -1)
        return res

example_solution = Solution()
input_nums = [3, 3, 4, 2, 4, 4, 2, 4, 4]

result = example_solution.majorityElement(input_nums)

print("Majority Element:", result)