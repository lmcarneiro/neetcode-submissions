class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev_row = [1] * n

        for row in range(m - 1):
            cur_row = [1] * n
            for col in range(n - 2, -1, -1):
                cur_row[col] = cur_row[col + 1] + prev_row[col]
            prev_row = cur_row

        return prev_row[0]