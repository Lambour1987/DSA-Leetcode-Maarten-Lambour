#2st Approach: Hashset/ Sliding Window
# Time: O(n*k)
# Space: O(n*k)

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        codeSet = set()

        for i in range(len(s) - k + 1):
            codeSet.add(s[i:i+k]) #zelf: wel logisch. start op i en tot k

        return len(codeSet) == 2 ** k #** betekend


s = "00110110"
k = 3

solution = Solution()
result = solution.hasAllCodes(s, k)
print(result)