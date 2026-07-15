#2st Approach: Hashset
# Time: O(10*1) --> O(1) to add on hashset. Overall O(n)
# Space: O(n): Every string has to go in hashset

class Solution:
    def findRepeatedDnaSequences(self, s:str)-> list[str]:
        seen, res = set(), set()

        for l in range(len(s)-9):
            cur = s[l:l + 10]
            if cur in seen:
                res.add(cur)
            #else statement maken niet nodig
            seen.add(cur)
        return list(res)

# Een instantie van de Solution-klasse maken
solution = Solution()

# Voorbeeldstring
s_example = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

# Herhaalde DNA-sequenties vinden
result = solution.findRepeatedDnaSequences(s_example)

# Het resultaat afdrukken
print("Herhaalde DNA-sequenties:", result)