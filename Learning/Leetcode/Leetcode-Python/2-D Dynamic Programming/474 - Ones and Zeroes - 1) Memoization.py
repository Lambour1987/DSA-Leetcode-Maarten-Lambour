#1st Approach: Memoization, cache = DP hashmap, dfs
# Time:
# Space:

class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        # Memoization
        dp = {}

        def dfs(i, m, n):
            if i == len(strs):
                return 0
            if (i, m, n) in dp:
                return dp[(i, m, n)]

            mCnt, nCnt = strs[i].count("0"), strs[i].count("1")
            dp[(i, m, n)] = dfs(i + 1, m, n)
            if mCnt <= m and nCnt <= n:
                dp[(i,m,n)] = max(
                    dp[(i, m, n)],
                    1 + dfs(i + 1, m - mCnt, n - nCnt))

            return dp[(i, m, n)]

        return dfs(0, m, n)

# Voorbeeld gebruik van de findMaxForm-methode
strings = ["10", "0001", "111001", "1", "0"]
m = 5
n = 3

# Maak een instantie van de Solution-klasse
oplossing = Solution()

# Roep de findMaxForm-methode aan
max_aantal_strings = oplossing.findMaxForm(strings, m, n)

# Print het maximale aantal strings dat kan worden geselecteerd
print("Maximaal aantal geselecteerde strings:", max_aantal_strings)