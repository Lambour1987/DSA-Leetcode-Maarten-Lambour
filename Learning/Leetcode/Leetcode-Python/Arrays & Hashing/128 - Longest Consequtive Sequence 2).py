#1st Approach: Sorted
# Time: O(nlogn)
# Space:

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums: #dus als je de elementen in de lijst zelf wilt gebruiken, en niet de index
            #check if its the start of a sequence
            if (n-1) not in numSet:
                length = 0
                while (n+length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

# Voorbeeldgebruik van de longestConsecutive-methode
solution = Solution()
nums = [100, 4, 200, 1, 3, 2, 5]

result = solution.longestConsecutive(nums)
print(result)



