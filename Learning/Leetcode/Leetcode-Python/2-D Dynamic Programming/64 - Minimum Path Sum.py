#1st Approach:
# Time:
# Space:

class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        res = [[float("inf")] * (COLS + 1) for r in range(ROWS +1)]
        res[ROWS-1][COLS] = 0

        for r in range(ROWS -1, -1, -1):
            for c in range(COLS -1, -1, -1):
                res[r][c] = grid[r][c] + min(res[r+1][c], res[r][c+1])

        return res[0][0]

# Voorbeeld gebruik van de minPathSum-methode
# Rooster
rooster = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]

# Maak een instantie van de Solution-klasse
oplossing = Solution()

# Roep de minPathSum-methode aan
minimale_som = oplossing.minPathSum(rooster)

# Print de minimale som van paden
print("Minimale som van paden:", minimale_som)