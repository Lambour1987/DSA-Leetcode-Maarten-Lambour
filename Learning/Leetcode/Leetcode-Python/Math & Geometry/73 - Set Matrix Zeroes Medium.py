class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        # O(1)
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False

        #determine which rows/ cols need to be zero
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0

                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True

        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0

# Maak een instantie van de Solution-klasse
oplossing = Solution()

# Voorbeeld matrix
matrix_voorbeeld = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 8, 9]
]

# Roep de setZeroes-methode aan
oplossing.setZeroes(matrix_voorbeeld)

# Print de matrix na het instellen van nullen
print("Matrix na instellen nullen:")
for row in matrix_voorbeeld:
    print(row)