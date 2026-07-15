#2st Approach: BruteForce
# Time: O(n*m)
# Space:


class Solution:
    def findDifferenceBruteforce(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        res1, res2 = [], []

        for n in nums1:
            found = False
            for m in nums2:
                if n == m:
                    found = True
                    break
            if not found:
                res1.append(n)

        for n in nums2:
            found = False
            for m in nums1:
                if n == m:
                    found = True
                    break
            if not found:
                res2.append(n)

        return [res1, res2]


# Voorbeeldgebruik voor de brute-force methode
solution = Solution()
nums1 = [1, 2, 3, 4, 5]
nums2 = [3, 4, 5, 6, 7]

resultaat_bruteforce = solution.findDifferenceBruteforce(nums1, nums2)
print(resultaat_bruteforce)