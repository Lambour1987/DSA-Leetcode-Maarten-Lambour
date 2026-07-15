class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []

        def backtrack(start, comb):
            if len(comb) == k:
                res.append(comb.copy())
                return

            for i in range(start, n + 1):
                comb.append(i)
                backtrack(i + 1, comb)
                comb.pop()
        backtrack(1, [])
        return res

solution = Solution()
result = solution.combine(4, 2)
print("Combinaties:", result)

# Een instantie van de Solution-klasse maken
solution = Solution()

# Voorbeeld van het genereren van combinaties voor n = 4 en k = 2
resultaat = solution.combine(4, 2)
print("Combinaties:", resultaat)