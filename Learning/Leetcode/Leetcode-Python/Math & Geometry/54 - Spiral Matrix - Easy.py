#1st Approach:
# Time: O(m*n)
# Space: O(1)

class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            #get every value in the top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            # get every i in the right column
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            if not (left < right and top < bottom):
                break

            #get every i in the bottom row
            for i in range(right - 1, left -1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            #get every i in the left col
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

        return res

# Voorbeeld gebruik van de spiralOrder-methode
matrix_voorbeeld = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Maak een instantie van de Solution-klasse
oplossing = Solution()

# Roep de spiralOrder-methode aan
resultaat = oplossing.spiralOrder(matrix_voorbeeld)

# Print het resultaat
print("Resultaat van spiralOrder:")
print(resultaat)