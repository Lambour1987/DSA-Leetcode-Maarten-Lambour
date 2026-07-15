#2st Approach:
# Time: O(1) -> dus ook niet sneller dan 1st approach
# Space:

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= (n-1)
            res += 1
        return res

solution = Solution()

# Voorbeeld
n = 11  # Binaire voorstelling: 1011
result = solution.hammingWeight(n)
print(result)  # Output: 3 (er zijn 3 '1'-bits in de binaire representatie van 11)