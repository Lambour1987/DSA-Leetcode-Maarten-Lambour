class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        # Log(n)
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l+r) // 2

            if target == nums[mid]:
                return mid

            if target > nums[mid]:
                l = mid + 1

            if target < nums [mid]:
                l = mid + 1
            else:
                r = mid - 1

        return l

# Maak een instantie van Solution
solution = Solution()

# Voorbeeld 1
nums1 = [1, 3, 5, 6]
target1 = 5
print("Voorbeeld 1:", solution.searchInsert(nums1, target1))  # Dit zou 2 moeten afdrukken

# Voorbeeld 2
nums2 = [1, 3, 5, 6]
target2 = 2
print("Voorbeeld 2:", solution.searchInsert(nums2, target2))  # Dit zou 1 moeten afdrukken

# Voorbeeld 3
nums3 = [1, 3, 5, 6]
target3 = 7
print("Voorbeeld 3:", solution.searchInsert(nums3, target3))  # Dit zou 4 moeten afdrukken

# Voorbeeld 4
nums4 = [1, 3, 5, 6]
target4 = 0
print("Voorbeeld 4:", solution.searchInsert(nums4, target4))  # Dit zou 0 moeten afdrukken