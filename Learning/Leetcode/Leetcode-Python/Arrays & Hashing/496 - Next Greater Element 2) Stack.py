#2nd Approach: Monotonic Stack
# Time: o(n+m)
# Space:

class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # O(n+m)
        nums1Idx = { n:i for i, n in enumerate(nums1)}
        res = [-1] * len(nums1)

        stack = []
        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and cur > stack[-1]:
                val = stack.pop()
                idx = nums1Idx[val]
                res [idx] = cur
            if cur in nums1Idx:
                stack.append(cur)
        return res




example = Solution()
nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]

result = example.nextGreaterElement(nums1, nums2)
print(result)
