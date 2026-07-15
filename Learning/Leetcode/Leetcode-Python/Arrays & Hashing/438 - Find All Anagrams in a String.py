#1st Approach: Hashmap, Sliding Window
# Time: O(s)
# Space:

#lijkt op LC 28

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(p) > len(s): return []
        pCount, sCount = {}, {}

        # Initieer pCount en sCount voor de eerste 'len(p)' karakters in s en p
        for i in range(len(p)):
            pCount[p[i]] = 1 + pCount.get(p[i], 0)
            sCount[s[i]] = 1 + sCount.get(s[i], 0)

        res = [0] if sCount == pCount else []
        l = 0

        for r in range(len(p), len(s)):
            sCount[s[r]] = 1 + sCount.get(s[r], 0)
            sCount[s[l]] -= 1
            l += 1

            if sCount[s[l - 1]] == 0:
                sCount.pop(s[l - 1])

            # Controleer of de anagramvoorwaarde geldt voor het huidige venster
            if sCount == pCount:
                res.append(l)

        return res

# Een instantie van de Solution-klasse maken
solution = Solution()

# Voorbeeld strings
s_example = "cbaebabacd"
p_example = "abc"

# Anagrammen vinden
result = solution.findAnagrams(s_example, p_example)

# Het resultaat afdrukken
print("De startindices van de anagrammen zijn:", result)







