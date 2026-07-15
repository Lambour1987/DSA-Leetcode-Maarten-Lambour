#2nd Approach: Dynamic Programming, caching result: Memoization
# Time: O(n) -> lineair time
# Space:

#Solving same subproblem. Niet uitgewerkt hier.

def climbStairs(n, memo={}):
    if n in memo:
        return memo[n]

    if n == 0 or n == 1:
        return 1
    else:
        ways = climbStairs(n - 1, memo) + climbStairs(n - 2, memo)
        memo[n] = ways
        return ways

# Voorbeeldgebruik
n = 4
result = climbStairs(n)
print(result)