class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r = 1, max(piles)
        min_k = r

        while l <= r:
            k = (r + l) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(float(p) / k)
            if hours > h:
                l = k + 1
            elif hours <= h:
                r = k - 1
                min_k = k

        return min_k