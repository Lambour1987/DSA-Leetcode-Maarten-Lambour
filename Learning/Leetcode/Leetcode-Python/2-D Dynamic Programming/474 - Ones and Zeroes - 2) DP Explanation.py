#2nd Approach: DP (zelf: True DP) Bottum to top ipv Top to bottum, reverse(zelf: tabulation)
# Time:
# Space:
from collections import defaultdict


class Solution:
    def findMaxForm(self, strs: list[str], M: int, N: int) -> int:
        # Dynamic Programming
        dp = defaultdict(int)

        for s in strs:
            mCnt, nCnt = s.count("0"), s.count("1")
            for m in range(M, mCnt -1, -1):
                for n in range(N, nCnt -1, -1):
                    dp[(m, n)] = max(
                        1 + dp[(m - mCnt, n-nCnt)],
                        dp[(m,n)])
        return dp[(M, N)]

# Voorbeeld gebruik van de findMaxForm-methode
strings = ["10", "0001", "111001", "1", "0"]
M = 5
N = 3

# Maak een instantie van de Solution-klasse
oplossing = Solution()

# Roep de findMaxForm-methode aan
max_aantal_strings = oplossing.findMaxForm(strings, M, N)

# Print het maximale aantal strings dat kan worden geselecteerd
print("Maximaal aantal geselecteerde strings:", max_aantal_strings)