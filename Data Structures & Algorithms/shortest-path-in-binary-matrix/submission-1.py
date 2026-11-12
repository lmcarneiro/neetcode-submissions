class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return - 1
        visit = set()
        q = deque()
        q.append((0, 0))
        visit.add((0, 0))
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]
        length = 1
        rows = cols = len(grid)
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                if (r, c) == (rows - 1, cols - 1):
                    return length
               
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr in range(rows) and nc in range(cols) and
                        grid[nr][nc] == 0 and (nr, nc) not in visit):
                        q.append((nr, nc))
                        visit.add((nr, nc))
            length += 1
                

        return -1