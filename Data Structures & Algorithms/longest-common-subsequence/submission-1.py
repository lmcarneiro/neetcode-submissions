class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if text1 == text2:
            return len(text1)

        dp = [[0 for j in range(len(text2) + 1)]
                 for i in range(len(text1) + 1)]

        M, N = len(text1), len(text2)

        for i in reversed(range(M)):
            for j in reversed(range(N)):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
        
        return dp[0][0]