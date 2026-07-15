#1st Approach:
# Time:
# Space:

#2nd Approach:
# Time:
# Space:

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for i in range(m-1):
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j+1] + row[j]
            row = newRow
        return row[0]

        # O(n * m) O(n)


# Voorbeeld gebruik van de uniquePaths-methode
# m = 3, n = 7
oplossing = Solution()
aantal_paden = oplossing.uniquePaths(3, 7)

# Print het aantal unieke paden
print("Aantal unieke paden:", aantal_paden)