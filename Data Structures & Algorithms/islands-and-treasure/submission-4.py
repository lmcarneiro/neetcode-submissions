class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        visited = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        INF = 2147483647

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))
        
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist

                for dr, dc in directions:
                    new_r = r + dr
                    new_c = c + dc
                    if new_r in range(rows) and new_c in range(cols) and grid[new_r][new_c] == INF:
                        q.append((new_r, new_c))
                        grid[new_r][new_c] = grid[r][c] + 1

            dist += 1