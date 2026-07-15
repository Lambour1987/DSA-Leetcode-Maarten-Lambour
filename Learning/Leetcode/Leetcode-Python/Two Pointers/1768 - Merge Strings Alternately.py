#1st Approach:
# Time: O(n+m)
# Space:

#appending & updating a string is not efficient. Just add strings as characters to array

class Solution:
    def mergeAlternately(self, word1: str, word2: str,) -> str:
        i, j = 0, 0

        res = []
        while i < len(word1) and j < len(word2):
            res.append(word1[i])
            res.append(word2[j])
            i = i + 1
            j = j + 1
        res.append(word1[i:])
        res.append(word2[j:])
        return "".join(res)

solution = Solution()
result = solution.mergeAlternately("abc", "def")
print(result)
