#1st Approach:
# Time:
# Space:

class Solution:
    def searcH(self, nums: list[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l<= r:
            m = l + (r - l) // 2
            if nums[m] == target: return True

            if nums[l] < nums[m]: # Left portion
                if nums[l] <= target < nums[m]:
                    r = m -1
                else:
                    l = m + 1
            elif nums[l] > nums[m]: # Right portion
                if nums[l] <= target < nums[m]:
                    r = m + 1
                else:
                    r = m - 1
            else:
                l += 1

        return False

# Maak een instantie van Solution
solution = Solution()

# Voorbeeld 1
nums1 = [2, 5, 6, 0, 0, 1, 2]
target1 = 0
result1 = solution.searcH(nums1, target1)
print(f"Is {target1} aanwezig in de array? {result1}")  # Dit zou True moeten afdrukken

# Voorbeeld 2
nums2 = [2, 5, 6, 0, 0, 1, 2]
target2 = 3
result2 = solution.searcH(nums2, target2)
print(f"Is {target2} aanwezig in de array? {result2}")  # Dit zou False moeten afdrukken

# Voorbeeld 3
nums3 = [1, 1, 1, 3, 1]
target3 = 3
result3 = solution.searcH(nums3, target3)
print(f"Is {target3} aanwezig in de array? {result3}")  # Dit zou True moeten afdrukken