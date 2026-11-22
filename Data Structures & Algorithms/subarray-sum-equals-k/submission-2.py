class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0

        prefix = {0: 1}
        total = 0

        for n in nums:
            total += n
            diff = total - k
            res += prefix.get(diff, 0)
            prefix[total] = 1 + prefix.get(total, 0)
        
        return res