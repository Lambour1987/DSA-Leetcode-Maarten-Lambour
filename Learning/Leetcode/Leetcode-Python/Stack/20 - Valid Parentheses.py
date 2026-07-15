class Solution:
    def isValid(self, s:str) -> bool:
        stack = []
        closeToOpen = { ")": "(", "]":"[", "}":"{"}

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False

# Een instantie van de Solution-klasse maken
solution = Solution()

# Voorbeeldstring
s1 = "()"
resultaat1 = solution.isValid(s1)
print(f"Is de string '{s1}' een geldige uitdrukking? {resultaat1}")

s2 = "()[]{}"
resultaat2 = solution.isValid(s2)
print(f"Is de string '{s2}' een geldige uitdrukking? {resultaat2}")

s3 = "(]"
resultaat3 = solution.isValid(s3)
print(f"Is de string '{s3}' een geldige uitdrukking? {resultaat3}")

s4 = "([)]"
resultaat4 = solution.isValid(s4)
print(f"Is de string '{s4}' een geldige uitdrukking? {resultaat4}")

s5 = "{[]}"
resultaat5 = solution.isValid(s5)
print(f"Is de string '{s5}' een geldige uitdrukking? {resultaat5}")