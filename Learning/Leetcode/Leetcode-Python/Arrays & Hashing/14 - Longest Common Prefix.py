#1st Approach:
# Time: O(n*m) -> where n is total number of characters * m different strings
# Space:

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        res = "" # Initialiseer de variabele res als een lege string. zelf: dus niet als []

        for i in range(len(strs[0])): #zelf: itereer (i) over ieder karakter in het eerste woord (dus over flower met index 0 tm 5)
            for s in strs: #itereer over elk woord 's'
                if i == len(s) or s[i] != strs[0][i]: #first check if out of bound.
                    return res
            res += strs[0][i] #[0] is het eerste woord. [i] is het eerste karakter van het eerste woord.

        return res

# Maak een instantie van de Solution-klasse
solution = Solution()

# Definieer een lijst met strings
strings = ["flower", "flow", "flight"]

# Roep de longestCommonPrefix-methode aan met de lijst strings als argument
result = solution.longestCommonPrefix(strings)

# Druk het resultaat af
print("Longest common prefix:", result)  # Dit zal "fl" afdrukken omdat dit het langste gemeenschappelijke voorvoegsel is