#1st Approach:
# Time:
# Space:

#2nd Approach:
# Time:
# Space:

class Solution:
    def countBits(self, n: int) -> list[int]:
        dp = [0] * (n+1)
        offset = 1

        for i in range(1, n+1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i- offset]

        return dp

solution = Solution()

# Voorbeeld
n = 5
result = solution.countBits(n)
print(result)  # Output: [0, 1, 1, 2, 1, 2]