class Solution:
    def findMin(self, nums: list[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l+r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res

# Maak een instantie van Solution
solution = Solution()

# Voorbeeld 1
nums1 = [3, 4, 5, 1, 2]
result1 = solution.findMin(nums1)
print(f"Het minimumelement is: {result1}")  # Dit zou 1 moeten afdrukken

# Voorbeeld 2
nums2 = [4, 5, 6, 7, 0, 1, 2]
result2 = solution.findMin(nums2)
print(f"Het minimumelement is: {result2}")  # Dit zou 0 moeten afdrukken

# Voorbeeld 3
nums3 = [11, 13, 15, 17]
result3 = solution.findMin(nums3)
print(f"Het minimumelement is: {result3}")  # Dit zou 11 moeten afdrukken