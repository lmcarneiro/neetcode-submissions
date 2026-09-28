class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict
        cols = defaultdict(set)
        sub = defaultdict(set)
        for i in range(len(board)):
            row = set()
            for j in range(len(board)):
                s = (i // 3) * 3 + (j // 3)
                if board[i][j] == '.':
                    continue
                if board[i][j] in row or board[i][j] in cols[j] or board[i][j] in sub[s]:
                    return False
                
                row.add(board[i][j])
                cols[j].add(board[i][j])
                sub[s].add(board[i][j])
        return True