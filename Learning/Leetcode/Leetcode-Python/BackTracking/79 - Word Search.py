#1st Approach: Bruteforce: Backtracking (niet uitgewerkt hier)
# Time: O(m*n*dfs): dus omvang board en steeds oproepen dfs(call stack: lenght word)
# Space:

#2st Approach: Bruteforce: Recursive (DFS) Backtracking
# Time:
# Space:

class Solution:
    def exist(self,board: list[list[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i): #row, column, current pointer i
            if i == len(word):
                return True
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                word[i] != board[r][c] or
                (r, c) in path
            ):
                return False

            path.add((r, c))
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r,c - 1, i + 1)
            )
            path.remove((r,c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0): return True

        return False

example_board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]

# Een instantie van de Solution-klasse maken
solution = Solution()

# Testen of het woord "ABCCED" in het bord voorkomt
word1 = "ABCCED"
result1 = solution.exist(example_board, word1)
print(f"Komt het woord '{word1}' voor in het bord? {result1}")

# Testen of het woord "SEE" in het bord voorkomt
word2 = "SEE"
result2 = solution.exist(example_board, word2)
print(f"Komt het woord '{word2}' voor in het bord? {result2}")

# Testen of het woord "ABCB" in het bord voorkomt
word3 = "ABCB"
result3 = solution.exist(example_board, word3)
print(f"Komt het woord '{word3}' voor in het bord? {result3}")