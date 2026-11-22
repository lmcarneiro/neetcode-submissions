class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        total = 0
        res = 0
        prefix = { 0: 1 }

        for n in nums:
            total += n
            remainder = total % k
            res += prefix.get(remainder, 0)
            prefix[remainder] = 1 + prefix.get(remainder, 0)

        return res