class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        #x is heaviest
        #y is second heaviest
        heapq.heapify_max(stones)
        while len(stones) > 1:
            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)

            if x > y:
                x -= y
                heapq.heappush_max(stones, x)
        if stones:
            return stones[0]
        else:
            return 0
        