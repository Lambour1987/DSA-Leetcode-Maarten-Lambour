#1st Approach: 1 Pointer i, shift it
# Time:
# Space:

# Remove en put in place
# Lijkt op partition, quicksort

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0 # is een variabele, geen pointer: Want geeft aan het eind de uitkomst aan. i is de pointer

        for i in range(len(nums)): #itereer door lijst nums. Zelf: je bent geinteresseerd in de index
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1 #is gelijk aan k = k + 1 is een teller die bijhoudt hoeveel elementen in de lijst niet gelijk zijn aan de waarde die moet worden verwijdert.
        return k

example_solution = Solution()
nums = [3, 2, 2, 3, 9, 11, 111, 205, 89, 48, 3 ,3 , 8,45, 26,3]
val = 3

new_length = example_solution.removeElement(nums, val)

print("Modified list:", nums[:new_length])
print("New length:", new_length)