class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]

        stack = []
        for p, s in sorted(pair)[::-1]: # Reverse Sorted Order
            stack. append((target -p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

solution = Solution()

# Voorbeeld invoer
target = 12
positions = [10, 8, 0, 5, 3]
speeds = [2, 4, 1, 1, 3]

# Roep de methode carFleet aan
number_of_fleets = solution.carFleet(target, positions, speeds)

print("Het aantal car fleets dat het doel zal bereiken is:", number_of_fleets)