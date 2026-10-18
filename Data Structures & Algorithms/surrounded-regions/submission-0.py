class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        def dfs(r, c):
            if r not in range(rows) or c not in range(cols) or board[r][c] != "O":
                return
            board[r][c] = "T"
            for dr, dc in directions:
                row, col = r + dr, c + dc
                dfs(row, col)

        for r in range(rows):
            for c in range(cols):
                if (board[r][c] == "O" and
                    (r in [0, rows -1] or c in [0, cols - 1])):
                    dfs(r, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"


