#1st Approach:
# Time: O(n)
# Space:

class Solution:
    def tribonacci(self, n:int) -> int:
        t = [0,1,1]

        if n < 3:
            return t[n]

        for i in range(3, n+ 1):
            t[0], t[1], t[2] = t[1], t[2], sum(t)
        return t[2]


# Voorbeeldgebruik
solution = Solution()

# Voorbeeld 1
result1 = solution.tribonacci(4)
print(result1)  # Output: 4

# Voorbeeld 2
result2 = solution.tribonacci(25)
print(result2)  # Output: 1389537