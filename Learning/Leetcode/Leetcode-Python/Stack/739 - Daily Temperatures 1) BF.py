#1st Approach:
# Time: O(n^2)
# Space:

#Monotonic decreasing order Stack
# Monotinc = decreasing

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0] * len(temperatures)
        stack = [] # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append([t, i])
        return res


solution = Solution()
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(solution.dailyTemperatures(temperatures))  # Uitvoer: [1, 1, 4, 2, 1, 1, 0, 0]
