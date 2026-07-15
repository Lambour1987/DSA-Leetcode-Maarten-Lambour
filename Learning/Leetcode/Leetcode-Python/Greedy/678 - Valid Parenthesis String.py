#1st Approach: Brute Force: Decision Tree
# Time:
# Space:

#zelf: niet met een stack? Klopt nog niet!!

class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0,0

        for c in s:
            if c =="(":
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif c == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:
                leftMin, leftMax = leftMin - 1, leftMax + 1
            if leftMax < 0:
                return False


        return leftMin == 0

# Een instantie van de Solution-klasse maken
solution = Solution()

# Voorbeeldstrings
s1 = "()"
resultaat1 = solution.checkValidString(s1)
print(f"Is de string '{s1}' geldig? {resultaat1}")

s2 = "(*)"
resultaat2 = solution.checkValidString(s2)
print(f"Is de string '{s2}' geldig? {resultaat2}")

s3 = "(*))"
resultaat3 = solution.checkValidString(s3)
print(f"Is de string '{s3}' geldig? {resultaat3}")