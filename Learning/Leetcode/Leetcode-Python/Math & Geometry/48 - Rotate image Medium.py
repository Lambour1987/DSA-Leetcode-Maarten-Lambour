#1st Approach:
# Time: O(n^2)
# Space: O(1)

class Solution:
    def rotate(self, matrix: list(list[int])) -> None:
        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r-1):
                top, bottom = l, r

                # save the topLeft
                topLeft = matrix[top][l + i]

                # move bottom left into top left
                matrix[top][l + i] = matrix[bottom - i][l]

                # move bottom right into bottom left
                matrix[bottom-i][l] = matrix[bottom][r-i]

                # move top right into bottom right
                matrix[bottom][r-i] = matrix[top + i][r]

                # move top Left into top right
                matrix[top + i][r] = topLeft
            r -= 1
            l += 1

# Voorbeeld gebruik van de rotate-methode
matrix_voorbeeld = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Maak een instantie van de Solution-klasse
oplossing = Solution()

# Roep de rotate-methode aan
oplossing.rotate(matrix_voorbeeld)

# Print het resultaat
print("Resultaat na rotatie:")
for row in matrix_voorbeeld:
    print(row)
