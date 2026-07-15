#1st Approach:
# Time:
# Space:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n

        while True:
            m = (l + r) // 2
            res = guess(m)
            if res > 0:
                l = m + 1
            elif res < 0:
                r = m - 1
            else:
                return m

# Externe functie guess - Je moet deze implementeren of aanpassen op basis van je specifieke gebruikssituatie
def guess(num: int) -> int:
    target_number = 42  # Dit is slechts een voorbeeld, vervang het door het werkelijke doelgetal
    if num == target_number:
        return 0
    elif num < target_number:
        return 1
    else:
        return -1

# Maak een instantie van Solution
solution = Solution()

# Voorbeeld - Raad het nummer
target_number_to_guess = 42
result = solution.guessNumber(target_number_to_guess)

# Controleer het resultaat
if result == 0:
    print("Het geraden nummer is correct:", target_number_to_guess)
else:
    print("Het geraden nummer is niet correct.")