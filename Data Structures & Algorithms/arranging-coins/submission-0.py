class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1
        while n:
            if n < i:
                break
            n -= i
            i += 1
        return i - 1