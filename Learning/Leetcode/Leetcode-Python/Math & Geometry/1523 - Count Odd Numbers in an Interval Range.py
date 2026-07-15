#1st Approach: BruteForce
# Time: O(n): Iterate through entire range
# Space:

#2nd Approach:
# Time: O(1)
# Space:

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        length = high - low + 1
        count = length // 2
        if length % 2 and low % 2:
            count += 1
        return count

# Een instantie van de Solution-klasse maken
solution = Solution()

# Voorbeeld van het tellen van oneven getallen in het bereik [3, 7]
low = 3
high = 7
resultaat = solution.countOdds(low, high)
print(f"Aantal oneven getallen in het bereik [{low}, {high}]: {resultaat}")