#1st Approach:
# Time: O(n) -> size of inputstring
# Space: O(n) -> size of stack in WC

#O(1) Pushing & Popping
#zelf wel een goed voorbeeld om stack te leren

#zou met string kunnen maar strings zijn immutable. Dus niet constant maar O(n)

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for c in s:
            if c == "*":
                stack and stack.pop() #zou ook met if else kunnen ipv stack and stack.pop (om te checken of stack leeg is)
            else:
                stack.append(c)
        return "".join(stack)

solution = Solution()
s = "ab*cd**e"
result = solution.removeStars(s)
print(result)  # Uitvoer: "ae"