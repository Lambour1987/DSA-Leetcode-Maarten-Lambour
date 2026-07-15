#1st Approach:
# Time:
# Space:

class Solution:
    def intToRoman(self, num: int) -> str:
        symList = [["I",1],["IV",4],["V",5],["IX",9],
                    ["X",10],["XL",40],["L",50],["XC",90],
                    ["C", 100], ["CD",400],["D",500],["CM",900],
                    ["M",1000]]

        #nu een list ipv hashmap omdat volgorde belangrijk is itt lc13

        res = ""
        for sym, val in reversed(symList):
            if num // val:
                count = num // val #// is delen
                res += (sym * count) #is gelijk aan res = res + (sym * count)
                num = num % val
        return res

# Een instantie van de Solution-klasse maken
solution = Solution()

# Voorbeeld van het omzetten van een decimaal getal naar Romeins voor num = 58
num1 = 58
resultaat1 = solution.intToRoman(num1)
print(f"Het Romeinse equivalent van {num1} is '{resultaat1}'")

# Voorbeeld van het omzetten van een decimaal getal naar Romeins voor num = 1994
num2 = 1994
resultaat2 = solution.intToRoman(num2)
print(f"Het Romeinse equivalent van {num2} is '{resultaat2}'")


