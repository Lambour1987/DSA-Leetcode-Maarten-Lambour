#1st Approach: Recusively with stack, backtrack
# Time:
# Space:

#2nd Approach:
# Time:
# Space:

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        # only add open parenthesis if open < n
        # only add a closing parenthesis if closed < open
        # valid IIF open == closed == n

        stack = []
        res =[]

        def backtrack(openN, closedN):
            if openN == closedN ==n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()

            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return res


# Een instantie van de Solution-klasse maken
solution = Solution()

# Voorbeeld van het genereren van haakjesparentheses voor n=3
n = 3
resultaat = solution.generateParenthesis(n)
print(f"Mogelijke combinaties van haakjesparentheses voor n={n}: {resultaat}")