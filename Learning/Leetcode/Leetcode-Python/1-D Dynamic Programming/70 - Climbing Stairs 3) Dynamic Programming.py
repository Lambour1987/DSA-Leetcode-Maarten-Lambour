#3nd Approach: Dynamic Programming, True DP: Bottum Up from base case. Store result in array
# Time:
# Space:

# Deze uitwerken

#3nd Approach
class Solution:
    def climbingStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n-1): #n is integer dus bijv 5.
            temp = one #zelf: voglens mij is temp de DP cache
            one = one + two
            two = temp

        return one

solution = Solution()

# Voorbeeld 1: n = 2
result1 = solution.climbingStairs(2)
print(f"Aantal manieren om een trap met 2 treden te beklimmen: {result1}")

# Voorbeeld 2: n = 5
result2 = solution.climbingStairs(5)
print(f"Aantal manieren om een trap met 5 treden te beklimmen: {result2}")