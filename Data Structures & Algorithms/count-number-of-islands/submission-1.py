class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        positions = set()
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            positions.add((r, c))
            grid[r][c] = "0"
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == "1" and 
                        (r, c) not in positions):

                        q.append((r, c))
                        positions.add((r, c))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in positions:
                    bfs(row, col)
                    islands += 1
        return islands

        
