#1st Approach: Brute Force
# Time: O(n^2)
# Space:

#2nd Approach: Two pointers
# Time:
# Space:

#1st Approach: Bruteforce: de r en l staan voor de hoogten(waarden van de index) van de balken (volgens mij).
# je pakt eerste alle waarden uit de reeks (l) en vervolgens alle waarden minus 1 (r). en dan bereken je het verschil.

class Solution:
    def maxArea(self, height: list[int]) -> int: #height is dus de hoogte (dus gewoon indexwaarden).
        # Brute Force
        res = 0

        for l in range(0, len(height)): #zelf erbij gezet '0,' dit is standaard dus hoef je niet neer te zetten. Begint dus bij index 0 (logisch)
            for r in range(l + 1, len(height)): #eerste iteratie begint r bij l + 1
                area = (r - 1) * min(height[l], height[r])
                res = max(res, area)

        return res

# Een instantie van de Solution-klasse maken
solution = Solution()

# Voorbeeld hoogten van de lijnen
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

# Testen van de maxArea-methode
resultaat = solution.maxArea(height)
print(f"Het maximale wateroppervlak is: {resultaat}")