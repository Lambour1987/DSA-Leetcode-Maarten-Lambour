#1st Approach:
# Time:
# Space:

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        for i in range(len(text1) -1, -1, -1):
            for j in range(len(text2) -1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])

        return dp[0][0]

# Voorbeeld gebruik van de longestCommonSubsequence-methode
# Strings
text1 = "abcde"
text2 = "ace"

# Maak een instantie van de Solution-klasse
oplossing = Solution()

# Roep de longestCommonSubsequence-methode aan
lengte_lcs = oplossing.longestCommonSubsequence(text1, text2)

# Print de lengte van de langste gemeenschappelijke subsequentie
print("Lengte van de langste gemeenschappelijke subsequentie:", lengte_lcs)