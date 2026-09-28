class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        print(points)
        res = []
        heap = []
        heapq.heapify(res)

        for point in points:
            dist = math.sqrt(point[0]**2 + point[1]**2)
            heapq.heappush(heap, (dist, point))

        print(heap)

        for i in range(k):
            dist, point = heapq.heappop(heap)
            res.append(point)

        return res