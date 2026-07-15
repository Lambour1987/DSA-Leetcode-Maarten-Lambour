#1st Approach: BruteForce by ChatGPT
# Time:
# Space:

class Solution:
    def leastBricks(self, wall: list[list[int]]) -> int:
        min_bricks = float('inf')

        for cut_point in range(1, sum(wall[0])):
            bricks_cut = 0

            for row in wall:
                current_width = 0
                for brick in row:
                    current_width += brick
                    if current_width == cut_point:
                        bricks_cut += 1
                        break
                    elif current_width > cut_point:
                        break

            min_bricks = min(min_bricks, len(wall) - bricks_cut)

        return min_bricks

# Voorbeeld van een muur
wall_example = [
    [1, 2, 2, 1],
    [3, 1, 2],
    [1, 3, 2],
    [2, 4],
    [3, 1, 2],
    [1, 3, 1, 1]
]

# Een instantie van de Solution-klasse maken
solution = Solution()

# Het minimaal aantal snijpunten met de minste bakstenen vinden
result = solution.leastBricks(wall_example)

# Het resultaat afdrukken
print("Het minimaal aantal snijpunten met de minste bakstenen is:", result)