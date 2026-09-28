class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        l = 0
        r = k
        while r < len(nums) + 1:
            win = nums[l:r]
            res.append(max(win))
            l += 1
            r += 1
        return res