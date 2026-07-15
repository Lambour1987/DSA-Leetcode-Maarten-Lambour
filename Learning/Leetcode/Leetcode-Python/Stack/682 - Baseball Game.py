#1st Approach:
# Time:
# Space:

class Solution:
    def calPoints(self, ops: list[str]) -> int:
        stack = []

        for op in ops:
            if op == "+":
                stack.append(stack[-1] + stack[-2])
            elif op == "D":
                stack.append(2 * stack[-1])
            elif op == "C":
                stack.pop()
            else:
                stack.append(int(op))

        return sum(stack)

# Maak een instantie van Solution
solution = Solution()

# Voorbeeld 1
ops1 = ["5","2","C","D","+"]
print("Voorbeeld 1:", solution.calPoints(ops1))  # Dit zou 30 moeten afdrukken

# Voorbeeld 2
ops2 = ["1","D","D","D"]
print("Voorbeeld 2:", solution.calPoints(ops2))  # Dit zou 15 moeten afdrukken

# Voorbeeld 3
ops3 = ["10","D","+","C"]
print("Voorbeeld 3:", solution.calPoints(ops3))  # Dit zou 5 moeten afdrukken