#1st Approach: Recursively, DFS, basecase
# Time:
# Space:

#2nd Approach:
# Time:
# Space:

#Zelf: de functies pop en append komen hier voor omdat het om backtracking gaat

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []

        def dfs(i, cur, total): #pointer i, single variable cur, total sum
            if total == target: #Basecase
                res.append(cur.copy()) #current toevoegen aan resultaat (=res). Kopie gebruiken omdat we cur blijven gebruiken.
                return
            if i >= len(candidates) or total > target: #Andere basecase
                return

            cur.append(candidates[i]) #cur is de variabele. Je voegt de huidige waarde behorend bij de index toe aan cur.
            dfs(i, cur, total + candidates[i]) #de functie dfs wordt opgeroepen met de argumenten
            cur.pop() #element verwijderen
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res

solution = Solution()

# Voorbeeld
candidates = [2, 3, 6, 7]
target = 7
result = solution.combinationSum(candidates, target)
print("Combinaties die de som 7 hebben:", result)
