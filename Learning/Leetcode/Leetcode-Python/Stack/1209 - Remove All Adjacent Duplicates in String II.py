class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []  # [char, count]

        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
            else:
                stack.append([c, 1])

            if stack[-1][1] == k:
                stack.pop()

        res = ""
        for char, count in stack:
            res += (char * count)
        return res

# Voorbeeld van het gebruik van de removeDuplicates-methode
solution = Solution()

# Voorbeeld invoer
s = "deeedbbcccbdaa"
k = 3

# Roep de methode removeDuplicates aan
result = solution.removeDuplicates(s, k)

print("Oorspronkelijke string:", s)
print("Na het verwijderen van duplicaten van", k, "opeenvolgende tekens, wordt de string:", result)