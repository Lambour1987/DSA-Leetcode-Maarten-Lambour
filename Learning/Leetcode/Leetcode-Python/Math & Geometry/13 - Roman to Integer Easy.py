#1st Approach: Hashmap
# Time: O(n)
# Space: O(1) Hashmap just have 7 values

class Solution:
    def romanToInt(self, s: str) -> int:

        roman = { "I": 1, "V":5, "X": 10,
                  "L": 50, "C": 100, "D": 500, "M": 1000}

        res = 0

        for i in range(len(s)):
            if i + 1 < len(s) and roman[s[i]] < roman[s[i+1]]:
                res -= roman[s[i]]
            else:
                res += roman[s[i]]

        return res

# Een instantie van de Solution-klasse maken
solution = Solution()

# Voorbeeld van het omzetten van een Romeins getal naar decimaal voor s = "III"
s1 = "III"
resultaat1 = solution.romanToInt(s1)
print(f"Het decimale equivalent van '{s1}' is {resultaat1}")

# Voorbeeld van het omzetten van een Romeins getal naar decimaal voor s = "IV"
s2 = "IV"
resultaat2 = solution.romanToInt(s2)
print(f"Het decimale equivalent van '{s2}' is {resultaat2}")

# Voorbeeld van het omzetten van een Romeins getal naar decimaal voor s = "IX"
s3 = "IX"
resultaat3 = solution.romanToInt(s3)
print(f"Het decimale equivalent van '{s3}' is {resultaat3}")

# Voorbeeld van het omzetten van een Romeins getal naar decimaal voor s = "LVIII"
s4 = "LVIII"
resultaat4 = solution.romanToInt(s4)
print(f"Het decimale equivalent van '{s4}' is {resultaat4}")

# Voorbeeld van het omzetten van een Romeins getal naar decimaal voor s = "MCMXCIV"
s5 = "MCMXCIV"
resultaat5 = solution.romanToInt(s5)
print(f"Het decimale equivalent van '{s5}' is {resultaat5}")