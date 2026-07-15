#2st Approach: Dynamic Programming, Cache
# Time: O(n*m)
# Space: O(n)

class Solution:
    def uniquePathsWithObstacles(self, grid: list[list[int]]) -> int:
        M, N = len(grid), len(grid[0])
        dp = [0] * N
        dp [N-1] = 1

        # Time: O(N*M), Space: O(N)
        for r in reversed(range(M)):
            for c in reversed(range(N)):
                if grid[r][c]:
                    dp[c] = 0
                elif c + 1 < N:
                    dp[c] = dp[c] + dp[c+1]
                else:
                    dp[c] = dp[c] + 0
        return dp[0]

# Voorbeeld gebruik van de uniquePathsWithObstacles-methode
# Rooster met obstakels
rooster_met_obstakels = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]

# Maak een instantie van de Solution-klasse
oplossing = Solution()

# Roep de uniquePathsWithObstacles-methode aan
aantal_paden = oplossing.uniquePathsWithObstacles(rooster_met_obstakels)

# Print het aantal unieke paden
print("Aantal unieke paden met obstakels:", aantal_paden)