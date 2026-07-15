#2st Approach: Hashmap, Count
# Time:
# Space

#Count Gaps. Max gaps is best solution

class Solution:
    def leastBricks(self, wall:list[list[int]]) -> int:
        countGap = {0:0} #mapping pos : count of brick gaps

        for r in wall:
            total = 0
            for b in r[:-1]: #laatste GAP niet meenemen
                total += b #total refers to position
                countGap[total] = 1 + countGap.get(total, 0) #0 is default value if total niet opgehaald kan worden

        return len(wall) - max(countGap.values()) #maximum uit hashmap halen


# Voorbeeld van een muur
wall_example = [
    [1, 2, 2, 1],
    [3, 1, 2],
    [1, 3, 2],
    [2, 4],
    [3, 1, 2],
    [1, 3, 1, 1]
]

# Een instantie van de Solution-klasse maken
solution = Solution()

# Het minimaal aantal snijpunten met de minste bakstenen vinden
result = solution.leastBricks(wall_example)

# Het resultaat afdrukken
print("Het minimaal aantal snijpunten met de minste bakstenen is:", result)

