#1st Approach:
# Time: O(n)
# Space:

class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        i = 0
        stack = []
        for n in pushed:
            stack.append(n)
            while i < len(popped) and stack and popped[i] == stack[-1]:
                stack.pop()
                i += 1
        return not stack

solution = Solution()
pushed = [1, 2, 3, 4, 5]
popped = [4, 5, 3, 2, 1]
print(solution.validateStackSequences(pushed, popped))  # Uitvoer: True