#1st Approach:
# Time:
# Space:

class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + ((r-1) // 2)
            if ((m - 1 < 0 or nums[m-1] != nums[m]) and
                (m + 1 == len(nums) or nums[m] !=nums[m+1])):
                return nums[m]

            leftSize = m - 1 if nums[m-1] == nums[m] else m
            if leftSize % 2:
                r = m - 1
            else:
                l = m + 1


# Maak een instantie van Solution
solution = Solution()

# Voorbeeld 1
nums1 = [1, 1, 2, 3, 3, 4, 4, 8, 8]
result1 = solution.singleNonDuplicate(nums1)
print(f"Het enkele niet-herhaalde element is: {result1}")  # Dit zou 2 moeten afdrukken

# Voorbeeld 2
nums2 = [3, 3, 7, 7, 10, 11, 11]
result2 = solution.singleNonDuplicate(nums2)
print(f"Het enkele niet-herhaalde element is: {result2}")  # Dit zou 10 moeten afdrukken

# Voorbeeld 3
nums3 = [1, 1, 2]
result3 = solution.singleNonDuplicate(nums3)
print(f"Het enkele niet-herhaalde element is: {result3}")  # Dit zou 2 moeten afdrukken