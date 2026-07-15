#1st Approach:
# Time:
# Space:

class Solution:
    def search(self, nums: list[int], target:int) -> int:
        l, r = 0, len(nums) - 1

        while l<= r:
            mid = (l+r) // 2
            if target == nums[mid]:
                return mid

            # left sorted portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # right sorted portion
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1

# Maak een instantie van Solution
solution = Solution()

# Voorbeeld 1
nums1 = [4, 5, 6, 7, 0, 1, 2]
target1 = 0
result1 = solution.search(nums1, target1)
print(f"Het doel {target1} is op positie {result1}")  # Dit zou 4 moeten afdrukken

# Voorbeeld 2
nums2 = [4, 5, 6, 7, 0, 1, 2]
target2 = 3
result2 = solution.search(nums2, target2)
print(f"Het doel {target2} is op positie {result2}")  # Dit zou -1 moeten afdrukken

# Voorbeeld 3
nums3 = [1]
target3 = 0
result3 = solution.search(nums3, target3)
print(f"Het doel {target3} is op positie {result3}")  # Dit zou -1 moeten
