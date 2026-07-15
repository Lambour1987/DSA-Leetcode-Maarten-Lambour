#1st Approach: door ChatGPT
# Time:
# Space:

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Helperfunctie om alle permutaties van een string te genereren
        def permutations(s):
            if len(s) <= 1:
                return [s]
            result = []
            for i, c in enumerate(s):
                for perm in permutations(s[:i] + s[i + 1:]):
                    result.append(c + perm)
            return result

        # Genereer alle permutaties van de eerste string
        perms = permutations(s)

        # Controleer of een van de permutaties gelijk is aan de tweede string
        for perm in perms:
            if perm == t:
                return True
        return False


# Voorbeeldgebruik
solution_instance = Solution()
s = "anagram"
t = "nagaram"
print(solution_instance.isAnagram(s, t))  # Output: True