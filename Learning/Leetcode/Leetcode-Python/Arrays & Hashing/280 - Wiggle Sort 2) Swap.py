#1st Approach: Sort & Swap
# Time: O(nlogn)
# Space:

class solution:
    def wiggleSort(self, nums):
        for i in range(1, len(nums)):
            if i % 2 == 1 and nums[i] >= nums[i-1]:
                nums[i], nums[i-1] = nums[i-1], nums[i] #kan ook met temporary variable
            if i % 2 == 0 and nums[i] >= nums[i-1]:
                nums[i], nums[i-1] = nums[i-1], nums[i]

# Voorbeeld gebruik
sol = solution()
nums = [3, 5, 2, 1, 6, 4]
print("Voor de wiggle sort:", nums)
sol.wiggleSort(nums)
print("Na de wiggle sort:", nums)