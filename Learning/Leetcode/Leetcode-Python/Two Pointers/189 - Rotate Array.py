#1st Approach:
# Time:
# Space:

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        k = k % len(nums)
        l, r = 0, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1

        l, r = 0, k-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r -1

        l, r = k, len(nums)-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1

example = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3

example.rotate(nums, k)
print(nums)