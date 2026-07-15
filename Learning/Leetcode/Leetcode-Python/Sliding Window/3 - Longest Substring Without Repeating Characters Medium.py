#1st Approach: BruteForce
# Time:
# Space:

#2nd Approach: Set for substring
# Time: O(n)
# Space: O(n)

class Solution:
    def lengthOfLongestSubstring(self, s:str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res

# Een instantie van de Solution-klasse maken
solution = Solution()

# Voorbeeldstring
s = "abcabcbb"

# Testen van de lengthOfLongestSubstring-methode
resultaat = solution.lengthOfLongestSubstring(s)
print(f"Lengte van de langste substring zonder herhalende karakters: {resultaat}")