class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(row, col):
            if (row in range(rows) and
                col in range(cols) and
                grid[row][col] == 1):

                grid[row][col] = 0


                return (1 + dfs(row + 1, col) +
                            dfs(row - 1, col) + 
                            dfs(row, col + 1) +
                            dfs(row, col - 1))
            return 0
                        

        for row in range(rows):
            for col in range(cols):
                max_area = max(dfs(row, col), max_area)

        return max_area
