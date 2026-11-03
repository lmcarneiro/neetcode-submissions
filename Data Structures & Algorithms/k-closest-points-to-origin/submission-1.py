class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for point in points:
            d = point[0]**2 + point[1] ** 2
            heapq.heappush(min_heap, (d, point))
        res = []
        for i in range(k):
            res.append(heapq.heappop(min_heap)[1])
        return res