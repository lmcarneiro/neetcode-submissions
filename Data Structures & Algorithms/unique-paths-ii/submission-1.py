class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * (cols + 1)
        dp[cols - 1] = 1

        for row in reversed(range(rows)):
            for col in reversed(range(cols)):
                if obstacleGrid[row][col]:
                    dp[col] = 0
                else:
                    dp[col] += dp[col + 1]

        return dp[0]