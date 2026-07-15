#1st Approach: BruteForce, Sliding window, nested forloops. Uitwerking door ChatGPT
# Time:
# Space:

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        if len(s) < 11:  # Er zijn geen herhaalde substrings als de lengte van de string minder dan 11 is
            return []

        seen = set()
        repeated = set()

        for i in range(len(s) - 9): #Startwaarde is dus s minus 9
            current_sequence = s[i:i + 10] #selectie substring van i t/m i + 10. Is sliding window
            if current_sequence in seen:
                repeated.add(current_sequence) #aan set toevoegen de huidige volgorde
            else:
                seen.add(current_sequence) #aan set toevoegen de huidige volgorde

        return list(repeated)

# Voorbeeldgegeven DNA-sequentie
s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
solution = Solution()
result = solution.findRepeatedDnaSequences(s)
print("Herhaalde DNA-sequenties van lengte 10:")
print(result)