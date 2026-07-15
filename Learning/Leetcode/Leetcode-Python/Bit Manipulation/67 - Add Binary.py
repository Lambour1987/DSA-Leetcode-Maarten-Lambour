#1st Approach: Lineair Algorithm
# Time:
# Space:



class Solution:
    def addBinary(self, a: str, b:str) -> str:
        res = ""
        carry = 0

        a, b = a[::-1], b[::-1]

        for i in range(max(len(a), len(b))):
            digitA = ord(a[i]) - ord("0") if i < len(a) else 0
            digitB = ord(b[i]) - ord("0") if i < len(b) else 0

            total = digitA + digitB + carry
            char = str(total % 2)
            res = char + res
            carry = total // 2

        if carry:
            res = "1" + res
        return res

# Een instantie van de Solution-klasse maken
solution = Solution()

# Voorbeeld van het optellen van binaire getallen voor a = "1010" en b = "1011"
a1, b1 = "1010", "1011"
resultaat1 = solution.addBinary(a1, b1)
print(f"De som van {a1} en {b1} in binaire vorm is '{resultaat1}'")

# Voorbeeld van het optellen van binaire getallen voor a = "110" en b = "1011"
a2, b2 = "110", "1011"
resultaat2 = solution.addBinary(a2, b2)
print(f"De som van {a2} en {b2} in binaire vorm is '{resultaat2}'")