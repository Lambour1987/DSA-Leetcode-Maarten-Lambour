#1st Approach: BF Hashmap
# Time: n^2 -> n*m (not search for every next greater element)
# Space:

class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # O(n*m)
        nums1Idx = { n:i for i, n in enumerate(nums1)}
        res = [-1] * len(nums1)

        for i in range(len(nums2)):
            if nums2[i] not in nums1Idx:
                continue
            for j in range(i + 1, len(nums2)):
                if nums2[j] > nums2[i]:
                    idx = nums1Idx[nums2[i]]
                    res[idx] = nums2[j]
                    break
        return res

example = Solution()
nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]

result = example.nextGreaterElement(nums1, nums2)
print(result)