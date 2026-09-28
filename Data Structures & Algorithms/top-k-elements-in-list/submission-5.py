class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []
        buckets = [[] for i in range(len(nums) + 1)]
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for num, cnt in count.items():
            buckets[cnt].append(num)

        i = 1
        while len(res) < k:
            while buckets[-i]:
                res.append(buckets[-i].pop())
            i += 1
        return res