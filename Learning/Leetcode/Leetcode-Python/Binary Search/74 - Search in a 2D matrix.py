#1st Approach:
# Time: O(m*n) board. Binary search log n. Dus O(m*logn)
# Space:

#2nd Approach:
# Time:
# Space:

class Solution:
    def searchMatrix(self, matrix: list(list[int]), target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        if not (top <= bot):
            return False
        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False

# Een instantie van de Solution-klasse maken
solution = Solution()

# Voorbeeldmatrix
voorbeeld_matrix = [
    [1, 4, 7, 11],
    [2, 5, 8, 12],
    [3, 6, 9, 16],
    [10, 13, 14, 17],
]

# Testen van de searchMatrix-methode
doelwit1 = 5
resultaat1 = solution.searchMatrix(voorbeeld_matrix, doelwit1)
print(f"Is het doelwit {doelwit1} aanwezig in de matrix? {resultaat1}")

doelwit2 = 20
resultaat2 = solution.searchMatrix(voorbeeld_matrix, doelwit2)
print(f"Is het doelwit {doelwit2} aanwezig in de matrix? {resultaat2}")