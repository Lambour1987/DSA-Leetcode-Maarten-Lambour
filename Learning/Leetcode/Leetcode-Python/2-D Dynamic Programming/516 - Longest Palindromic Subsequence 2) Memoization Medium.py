#2nd Approach: Also Dynamic Approach Brute Force, DFS,
# Recursive, Memoiazation, Cache(=Hashmap), Basecase
# Time: O(
# Space:
from pip._internal import cache


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        cache = {}

        def dfs (i,j):
            if i < 0 or j == len(s):
                return 0
            if (i, j) in cache:
                return cache[(i, j)]

            if s[i] == s[j]:
                length = 1 if i == j else 2
                cache[(i, j)] = length + dfs(i-1, j+1)

            else:
                cache[(i, j)] = max(dfs(i - 1, j), dfs(i,j+1))
            return cache[(i, j)]

        for i in range(len(s)):
            dfs(i, i) # odd length
            dfs(i, i + 1) # even length
        return max(cache.values())


# Voorbeeld gebruik van de longestPalindromeSubseq-methode
# String
s = "bbbab"

# Maak een instantie van de Solution-klasse
oplossing = Solution()

# Roep de longestPalindromeSubseq-methode aan
lengte_palindroom = oplossing.longestPalindromeSubseq(s)

# Print de lengte van de langste palindroom subsequention
print("Lengte van de langste palindroom subsequention:", lengte_palindroom)


