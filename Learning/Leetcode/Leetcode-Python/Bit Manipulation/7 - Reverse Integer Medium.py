#1st Approach:
# Time:
# Space:

import math

class Solution:
    def reverse(self, x: int) -> int:

        MIN = -2147483648 #-2^31
        MAX = 2147483647 #2^31 -1

        res = 0
        while x:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)

            if (res > MAX // 10 or
                    (res == MAX // 10 and digit >=MAX  % 10)):
                return 0
            if (res < MIN // 10 or
                    (res == MIN/ 10 and digit <= MIN %10)):
                return 0
            res = (res * 10) + digit

        return res

# Een instantie van de Solution-klasse maken
solution = Solution()

# Voorbeeld van het omkeren van een geheel getal voor x = 123
x1 = 123
resultaat1 = solution.reverse(x1)
print(f"Het omgekeerde van {x1} is {resultaat1}")

# Voorbeeld van het omkeren van een geheel getal voor x = -123
x2 = -123
resultaat2 = solution.reverse(x2)
print(f"Het omgekeerde van {x2} is {resultaat2}")

# Voorbeeld van het omkeren van een geheel getal voor x = 120
x3 = 120
resultaat3 = solution.reverse(x3)
print(f"Het omgekeerde van {x3} is {resultaat3}")
