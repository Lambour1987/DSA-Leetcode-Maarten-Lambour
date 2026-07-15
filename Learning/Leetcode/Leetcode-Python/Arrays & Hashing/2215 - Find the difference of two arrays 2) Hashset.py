#2nd Approach: Hashset
# Time: O(n*1) -> O(1) -> maar 2x dus O(n+m)
# Space:


class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        nums1Set, nums2Set = set(nums1), set(nums2)
        res1, res2 = [], []

        for n in nums1:
            if n not in nums2Set:
                res1.append(n)

        for n in nums2:
            if n not in nums1Set:
                res2.append(n)

        return [res1, res2]


# Voorbeeldgebruik
solution = Solution()
nums1 = [1, 2, 3, 4, 5]
nums2 = [3, 4, 5, 6, 7]

resultaat = solution.findDifference(nums1, nums2)
print(resultaat)