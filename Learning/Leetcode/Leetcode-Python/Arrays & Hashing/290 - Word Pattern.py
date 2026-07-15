#1th approach: Hashmap, splitfunction
# Time: O(n + m)
# Space: O(n + m)

#Edge Cases:

#Zie LC205, 290

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")                #eerst even alle spaties weghalen
        if len(pattern) !=len(words):       #vervolgens even checken of ze niet gelijk zijn
            return False

        charToWord = {}                     #Hashmapje 1
        wordToChar = {}                     #Hashmapje 2

        for c, w in zip(pattern, words):    #zip allows you to iterate through both strings at the same time
            if c in charToWord and charToWord[c] !=w: #getfunctie wordt hier nu niet gebruikt
                return False
            if w in wordToChar and wordToChar[w] !=c:
                return False

            charToWord[c] = w
            wordToChar[w] = c
        return True

solution = Solution()

# Voorbeeld 1
result1 = solution.wordPattern("abba", "dog cat cat dog")
print(f"Heeft het woordpatroon: {result1}")

# Voorbeeld 2
result2 = solution.wordPattern("abba", "dog cat cat fish")
print(f"Heeft het woordpatroon: {result2}")

# Voorbeeld 3
result3 = solution.wordPattern("aaaa", "dog cat cat dog")
print(f"Heeft het woordpatroon: {result3}")