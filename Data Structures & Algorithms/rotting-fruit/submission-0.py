class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        fresh = 0
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        mins = 0
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    new_r = r + dr
                    new_c = c + dc
                    if new_r in range(rows) and new_c in range(cols) and grid[new_r][new_c] == 1:
                        q.append((new_r, new_c))
                        fresh -= 1
                        grid[new_r][new_c] = 2

            mins += 1
        return mins if fresh == 0 else -1
