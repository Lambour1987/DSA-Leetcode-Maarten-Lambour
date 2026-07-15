

#1th approach: Two Pointers: compare the two strings # Dynamic Programming Problem
# Time: O(n): O(s+t)
# Space:

#: zelf: kijken of s is subsequence of t. Dus als s al langer is dan t, dan sowieso geen subsequence
# Zie ook LC169,242,392

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool: #Bool dus sowieso ergens Return True Or False
        i, j = 0, 0 #i itereert over s op index 0. j itereert over t op index 0
        #als we doen i,j = s[0],t[0] zou hetzelfde moeten gebeuren maar dan hebben we het echt over de waarden horend bij s[0] ipv de index.
        #heeft ook weer iets te maken met dat we een while loop gebruiken

        while i < len(s) and j <len(t): #dit is de voorwaarde om te kijken of de iteratie moet doorgaan
            if s[i] == t[j]:
                i += 1 #i = i + 1. Ja alleen dus i verschuiven als ze gelijk zijn (niet beide, want dan sla je mogelijk een letter over)
            j += 1 #dit is dus 'else'

        return True if i == len(s) else False

solution_instance = Solution()
result = solution_instance.isSubsequence("abc", "ahbgdc")
print(result)