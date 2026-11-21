class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        g_max = g_min = nums[0]
        cur_max = cur_min = 0
        total = 0

        for n in nums:
            cur_max = max(cur_max + n, n)
            cur_min = min(cur_min + n, n)
            total += n
            g_max = max(g_max, cur_max)
            g_min = min(g_min, cur_min)


        return max(g_max, total - g_min) if g_max > 0 else g_max