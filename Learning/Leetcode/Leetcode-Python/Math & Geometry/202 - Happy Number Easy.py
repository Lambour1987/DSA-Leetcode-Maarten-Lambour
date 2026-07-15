#1st Approach: Hashset
# Time:
# Space:

# er is een betere oplossing: linked list cycle. zie filmpje

class Solution:
    def isHappy(self, n:int) -> bool:
        visit = set()

        while n not in visit:
            visit.add(n)
            n = self.sumOfSquares(n)

            if n == 1:
                return True

        return False

    def sumOfSquares(self, n: int) -> int: # helper function
        output = 0

        while n:
            digit = n % 10
            digit = digit ** 2 #**2 is tot de macht 2
            output += digit
            n = n // 10 #// is integer division
        return output


# Voorbeeld gebruik van de isHappy-methode
getal = 19

# Maak een instantie van de Solution-klasse
oplossing = Solution()

# Roep de isHappy-methode aan
is_happy = oplossing.isHappy(getal)

# Print het resultaat
print(f"{getal} is een gelukkig getal: {is_happy}")