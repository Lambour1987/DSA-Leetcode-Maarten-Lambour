class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        cur = ""

        for c in path + "/":
            if c == "/":
                if cur == "..":
                    if stack: stack.pop()
                elif cur != "" and cur != ".":
                    stack.append(cur)
                cur = ""
            else:
                cur += c

        return "/" + "/".join(stack)

solution = Solution()

# Voorbeeld invoer
path = "/home//foo/"

# Roep de methode simplifyPath aan
simplified_path = solution.simplifyPath(path)

print("Vereenvoudigd pad is:", simplified_path)