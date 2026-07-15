#1st Approach:
# Time:
# Space:

#2nd Approach:
# Time:
# Space:

#Zie LC205, 290

class Solution:
    def isomorphicStrings(self, s: str, t:str) -> bool:
        mapST, mapTS = {}, {}

        for i in range(len(s)):
            c1, c2 = s[i], t[i]

            if ((c1 in mapST and mapST[c1] !=c2) or
                (c2 in mapTS and mapTS[c2] !=c1)):
                return False

            mapST[c1] = c2
            mapTS[c2] = c1

        return True

solution = Solution()

# Voorbeeld 1
result1 = solution.isomorphicStrings("egg", "add")
print(f"Zijn isomorf: {result1}")

# Voorbeeld 2
result2 = solution.isomorphicStrings("foo", "bar")
print(f"Zijn isomorf: {result2}")