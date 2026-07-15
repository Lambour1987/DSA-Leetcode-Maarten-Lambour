class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for c in num:
            while k >0 and stack and stack[-1] > c:
                k -= 1
                stack.pop()
            stack.append(c)

        stack = stack[:len(stack)-k]
        res = "".join(stack)
        return str(int(res)) if res else "0"


# Voorbeeld van het gebruik van de removeKdigits-methode
solution = Solution()

# Voorbeeld invoer
num = "1432219"
k = 3

# Roep de methode removeKdigits aan
result = solution.removeKdigits(num, k)

print("Oorspronkelijk nummer:", num)
print("Na het verwijderen van", k, "cijfers, wordt het nummer:", result)