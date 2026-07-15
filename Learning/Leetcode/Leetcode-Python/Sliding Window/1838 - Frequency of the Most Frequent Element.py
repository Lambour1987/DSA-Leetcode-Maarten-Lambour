#1st Approach: Sort
# Time: O(nlogn)
# Space:

#2nd Approach:
# Time:
# Space:

class Solution:
    def maxFrequency(self, nums:list[int], k: int) -> int:
        nums.sort()

        l, r = 0, 0
        res, total = 0, 0

        while r < len(nums):
            total += nums[r]

            while nums[r] * (r - l + 1)> total + k:
                total -= nums[l]
                l += 1
            res = max(res, r-l + 1)
            r += 1
        return res

# Een instantie van de Solution-klasse maken
solution = Solution()

# Voorbeeldlijst en tolerantie
nums = [1, 2, 4]
k = 5

# Testen van de maxFrequency-methode
resultaat = solution.maxFrequency(nums, k)
print(f"Lengte van het langste deel met de frequentie plus {k}: {resultaat}")