#1st Approach: Brute Force, Decision Tree, Recursion, DFS
# Time: 2^n
# Space:

#ChatGpt

def climbStairs(n):
    if n == 0 or n == 1:
        return 1
    else:
        return climbStairs(n - 1) + climbStairs(n - 2)

# Voorbeeldgebruik
n = 4
result = climbStairs(n)
print(result)