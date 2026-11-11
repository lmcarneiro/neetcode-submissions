class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = [-num for num in nums]
        heapq.heapify(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, -val)
        tmp = []
        for _ in range(self.k):
            r = heapq.heappop(self.nums)
            tmp.append(r)
        for num in tmp:
            heapq.heappush(self.nums, num)
        return -r

            

        
