#2nd Approach: Hashmap - Map value to index (zelf: key (index) to value)
# Time: O(n) (1 pass)
# Space: O(n)

#Zelf: Volgens mij heeft 2 pointers hier geen zin omdat de lijst niet per se gesorteerd is (in het vb wel)

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # val : index

        for i, n in enumerate(nums): # in andere code: for i in range(len(nums)). min of meer hetzelfde.
            # Enumerate: doorloop zowel elementen als indices (zelf: tegelijk)
            diff = target - n
            if diff in prevMap: #hier niet prevMap.get(n,0) oid omdat we hier een if statement gebruiken
                return [prevMap[diff], i] #zelf: dus [diff] is de variabele en , i de index.
            prevMap[n] = i
        return

example_nums = [2, 7, 11, 15]
example_target = 13
solution_instance = Solution()
result = solution_instance.twoSum(example_nums, example_target)
print(result)

#Zelf dus: indien niet gesorteerd: hashmap. Wel gesorteerd two pointers