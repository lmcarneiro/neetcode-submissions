class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        positions = set()
        max_area = 0
        island = 0
        rows, cols = len(grid), len(grid[0])

        def bfs(row, col, max_area, island):
            q = collections.deque()
            positions.add((row, col))
            grid[row][col] = 0
            q.append((row, col))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == 1 and
                        (r, c) not in positions):

                        island += 1
                        q.append((r,c))
                        positions.add((r, c))
            return max(max_area, island)
                        

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row, col) not in positions:
                    island = 1
                    max_area = bfs(row, col, max_area, island)

        return max_area
