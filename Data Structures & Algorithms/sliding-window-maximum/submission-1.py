class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        l = 0
        r = k
        for l in range(len(nums) - k + 1):
            win = nums[l:k+l]
            res.append(max(win))
        return res