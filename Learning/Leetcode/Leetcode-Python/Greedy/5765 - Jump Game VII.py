#1st Approach: Dynamic Programming
# Time: O(n*j)
# Space:

#2nd Approach: BFS
# Time: O(n)
# Space: O(n)

from collections import deque

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        q, farthest = deque([0]), 0

        while q:
            i = q.popleft()
            start = max(i + minJump, farthest + 1)
            for j in range(start, min(i + maxJump + 1, len(s))):
                if s[j] == "0":
                    q.append(j)
                    if j == len(s) - 1:
                        return True
            farthest = i + maxJump

solution = Solution()

# Voorbeeld
s = "011010"
minJump = 2
maxJump = 3
result = solution.canReach(s, minJump, maxJump)
print(result)  # Output: True