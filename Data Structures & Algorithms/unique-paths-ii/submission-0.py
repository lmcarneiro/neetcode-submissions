class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * (cols + 1)
        dp[cols - 1] = 1

        for row in range(rows - 1, -1, -1):
            for col in range(cols - 1, -1 ,-1):
                if obstacleGrid[row][col]:
                    dp[col] = 0
                else:
                    dp[col] += dp[col + 1]

        return dp[0]