#2nd Approach: Two Pointers: Lineair Time solution
# Time: O(n)
# Space:

class Solution:
    def maxArea(self, height: list[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1

        while l < r:
            area = (r-1) * min(height[l], height[r])
            res = max(res, area)

            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else:
                l +=1
                r -=1

        return res

# Een instantie van de Solution-klasse maken
solution = Solution()

# Voorbeeldhoogten van de lijnen
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

# Testen van de maxArea-methode
resultaat = solution.maxArea(height)
print(f"Het maximale wateroppervlak is: {resultaat}")