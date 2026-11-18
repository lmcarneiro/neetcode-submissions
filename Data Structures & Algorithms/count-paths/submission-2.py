class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev_row = [1] * n

        for r in reversed(range(m - 1)):
            cur_row = [1] * n
            for c in reversed(range(n - 1)):
                cur_row[c] = cur_row[c + 1] + prev_row[c]
            prev_row = cur_row

        return prev_row[0]