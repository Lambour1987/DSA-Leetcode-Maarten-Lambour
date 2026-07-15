#1st Approach:
# Time: O(n*n^1/2)
# Space:

#3/12/23: er is ook nog een snelerre, wiskundige methode om dit uit te werken. Niet nodig maar kan eens kijken voor de grap.

class Solution:
    def numSquares(self, n:int) -> int:
        dp = [n] * (n + 1)
        dp[0] = 0

        for target in range(1, n + 1):
            for s in range(1, target + 1):
                square = s * s
                if target - square < 0:
                    break
                dp[target] = min(dp[target], 1 + dp[target - square])

        return dp[n]



# Voorbeeld gebruik van de numSquares-methode
# Getal
getal = 12

# Maak een instantie van de Solution-klasse
oplossing = Solution()

# Roep de numSquares-methode aan
min_aantal_vierkanten = oplossing.numSquares(getal)

# Print het minimaal benodigde aantal perfecte vierkanten
print(f"Minimaal aantal perfecte vierkanten om {getal} te vormen: {min_aantal_vierkanten}")