class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_island = 0
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def dfs(row, col):

            if (row >= 0 and row < ROWS and col >= 0 and col < COLS and grid[row][col] == 1
                ):

                grid[row][col] = 0

                
                area = 1
                for dr, dc in directions:
                    new_row = row + dr
                    new_col = col + dc
                    area += dfs(new_row, new_col)

                return area

            return 0
            
        for row in range(ROWS):
            for col in range(COLS):
                max_island = max(dfs(row, col), max_island)
        
        return max_island