class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        res = []
        for i in nums:
            h[i] = 1 + h.get(i, 0)
        arr = []
        for key, value in h.items():
            arr.append([value, key])
        arr.sort()        
        while len(res) < k:
            res.append(arr.pop()[1])
        return res