class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        k = 1

        l, r = 1, max(piles)

        while l <= r:
            time = 0
            m = l + ((r - l) // 2)
            for pile in piles:
                time += math.ceil(pile / m)
            if time <= h:
                k = m
                r = m - 1
            else:
                l = m + 1
        return k
            
