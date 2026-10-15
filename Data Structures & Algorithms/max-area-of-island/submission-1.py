class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows, cols = len(grid), len(grid[0])

        def bfs(row, col, max_area):
            q = collections.deque()
            grid[row][col] = 0
            q.append((row, col))
            island = 1

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == 1):

                        island += 1
                        q.append((r,c))
                        grid[r][c] = 0

            return max(max_area, island)
                        

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    max_area = bfs(row, col, max_area)

        return max_area
