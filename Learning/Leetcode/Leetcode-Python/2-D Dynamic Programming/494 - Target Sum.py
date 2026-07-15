#1st Approach: DP, Recursive, Backtracking, Cache dmv Hashmap
# Time:
# Space:

class Solution:
    def findTargetSumWays(self, nums: list[int], target: int)-> int:
        dp = {} # (index, total) -> # of ways

        def backtrack(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in dp:
                return dp[(i, total)]

            dp[(i, total)] = (backtrack(i + 1, total + nums[i]) +
                              backtrack(i + 1, total - nums[i]))
            return dp[(i, total)]

        return backtrack(0, 0)

# Voorbeeld gebruik van de findTargetSumWays-methode
# Lijst van getallen
getallen = [1, 1, 1, 1, 1]
# Doelwit
doelwit = 3

# Maak een instantie van de Solution-klasse
oplossing = Solution()

# Roep de findTargetSumWays-methode aan
aantal_manieren = oplossing.findTargetSumWays(getallen, doelwit)

# Print het aantal manieren om het doelwit te bereiken
print(f"Aantal manieren om het doelwit {doelwit} te bereiken: {aantal_manieren}")