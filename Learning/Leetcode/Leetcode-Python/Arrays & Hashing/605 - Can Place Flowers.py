#1st Approach:
# Time: O(n)
# Space:

class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        f = [0] + flowerbed + [0] #toevoegen van een nul aan het begin en eind t.b.v. edge cases

        for i in range(1, len(f)-1): #skip first en last index
            if f[i-1] == 0 and f[i] == 0 and f[i+1]==0:
                f[i] = 1
                n -= 1
        return n <= 0



solution = Solution()
flowerbed = [1, 0, 0, 0, 1]
n = 1
result = solution.canPlaceFlowers(flowerbed, n)
print(result)