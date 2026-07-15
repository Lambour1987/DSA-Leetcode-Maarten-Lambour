#3th approach: Hashset
# Time: O(n)
# Space: O(n): because of hashset

#Zelf: Bucket?
#Dus inserten en checken voor waarden in hashset in O(1)

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums: #doorloop de waarden in nums (niet de index)
            if n in hashset:
                return True
            hashset.add(n) #n toevoegen aan hashset
        return False

solution_instance = Solution()
example_nums = [1,2,3,4,1]
result = solution_instance.containsDuplicate(example_nums)
print(result)