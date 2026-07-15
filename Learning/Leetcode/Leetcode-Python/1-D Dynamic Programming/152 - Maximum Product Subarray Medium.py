#1st Approach:
# Time: O(n^2)
# Space:

#2nd Approach:
# Time:
# Space:

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1

        for n in nums:
            if n == 0:
                curMin, curMax = 1,1
                continue
            tmp = curMax * n
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(tmp, n * curMin, n)
            res = max(res, curMax)
        return res

# Een instantie van de Solution-klasse maken
solution = Solution()

# Voorbeeld van een lijst met getallen
voorbeeld_nums = [2, 3, -2, 4]

# Testen van de maxProduct-methode
resultaat = solution.maxProduct(voorbeeld_nums)
print(f"Het maximale product is: {resultaat}")