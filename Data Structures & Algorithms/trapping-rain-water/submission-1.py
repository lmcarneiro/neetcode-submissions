class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        res = 0
        max_l = height[l]
        max_r = height[r]

        while l < r:
            if max_l < max_r:
                res += max(max_l - height[l], 0)
                l += 1
                max_l = max(max_l, height[l])
            else:
                res += max(max_r - height[r], 0)
                r -= 1
                max_r = max(max_r, height[r])
            
            
        return res