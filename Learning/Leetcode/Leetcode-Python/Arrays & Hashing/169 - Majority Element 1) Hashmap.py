#1st Approach: Hashmap. Count occurances: Counter
# Time: O(1) -> O(n): Iterate through entire array
# Space: O(n): Hashmap

#zie ook LC169,242,392

from typing import List

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = {} #hashmap
        res, maxCount = 0, 0 #result en maxcount

        for n in nums: #alleen als je geïnteresserd bent in de waarden, niet de index
            count[n] = 1 + count.get(n, 0) #Hier wordt aan de hashmap toegevoegd maar ook
            # uit de hashmap gehaald. 0 is default value, als er niks opgehaald wordt uit Hashmap. n is de key/waarde uit de hashmap
            res = n if count[n] > maxCount else res
            maxCount = max(count[n], maxCount)
        return res

example_solution = Solution()
input_nums = [3, 3, 4, 2, 4, 4, 2, 4, 4]

result = example_solution.majorityElement(input_nums)

print("Majority Element:", result)