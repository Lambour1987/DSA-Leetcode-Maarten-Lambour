#1st Approach: Brute Force. Decision Tree
# Time:
# Space:

#2nd Approach: Memoization
# Time:
# Space:

#3nd Approach: Dynamic Programming
# Time:
# Space:

# Deze uitwerken. Lijkt veel op LC70. You can't be greedy

#3nd Approach

from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        cost.append(0)

        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i+2])

        return min(cost[0], cost[1])

solution = Solution()

# Voorbeeld 1: kosten voor het beklimmen van trappen
cost1 = [10, 15, 20]
result1 = solution.minCostClimbingStairs(cost1)
print(f"Minimale kosten om de trap te beklimmen: {result1}")

# Voorbeeld 2: andere set van kosten
cost2 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
result2 = solution.minCostClimbingStairs(cost2)
print(f"Minimale kosten om de trap te beklimmen: {result2}")