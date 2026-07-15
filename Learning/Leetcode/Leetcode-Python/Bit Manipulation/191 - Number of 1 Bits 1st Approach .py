#1st Approach: logic AND operation(&) of m.b.v. modding% en integer division
# Time: O(32) -> O(1). (vanwege 32 bit integer)
# Space: O(1)

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n % 2
            n = n >> 1
        return res

solution = Solution()

# Voorbeeld
n = 11  # Binaire voorstelling: 1011
result = solution.hammingWeight(n)
print(result)  # Output: 3 (er zijn 3 '1'-bits in de binaire representatie van 11)