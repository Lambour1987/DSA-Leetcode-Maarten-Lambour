#1st Approach: Brute Force, Recursive, DFS, Hashmap for Cache
# Time: O(n*m)
# Space: O(n*m)

class Solution:
    def uniquePathsWithObstacles(self, grid: list[list[int]]) -> int:
        M, N = len(grid), len(grid[0])
        dp = {(M - 1, N- 1): 1}

        def dfs(r,c):
            if r == M or c == N or grid[r][c]:
                return 0
            if (r, c) in dp:
                return dp[(r, c)]
            dp[(r, c)] = dfs(r + 1, c) + dfs(r, c + 1)
            return dp[(r, c)]

        return dfs(0,0)


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