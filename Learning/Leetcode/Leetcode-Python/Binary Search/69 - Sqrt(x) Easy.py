#1st Approach:
# Time: logn
# Space:

class Solution:
    def mySqrt(self, x:int) -> int:
        l, r = 0, x
        res = 0

        while l <= r:
            m = l + ((r - l) // 2)
            if m**2 > x:
                r = m - 1
            elif m**2 < x:
                l = m + 1
                res = m
            else:
                return m

# Maak een instantie van Solution
solution = Solution()

# Voorbeeld 1
x1 = 16
result1 = solution.mySqrt(x1)
print(f"Vierkantswortel van {x1} is ongeveer {result1}")  # Dit zou 4 moeten afdrukken

# Voorbeeld 2
x2 = 8
result2 = solution.mySqrt(x2)
print(f"Vierkantswortel van {x2} is ongeveer {result2}")  # Dit zou 2 moeten afdrukken

# Voorbeeld 3
x3 = 25
result3 = solution.mySqrt(x3)
print(f"Vierkantswortel van {x3} is ongeveer {result3}")  # Dit zou 5 moeten afdrukken