class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        for p in [2, 3, 5]:
            while n % p == 0:
                n = n // p
        return n == 1

# Voorbeeld gebruik van de isUgly-methode
getal = 14

# Maak een instantie van de Solution-klasse
oplossing = Solution()

# Roep de isUgly-methode aan
is_ugly = oplossing.isUgly(getal)

# Print het resultaat
print(f"{getal} is een lelijk getal: {is_ugly}")