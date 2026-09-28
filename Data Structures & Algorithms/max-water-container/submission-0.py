class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l, r = 0, len(heights) - 1
        
        while l < len(heights) - 1:
            
            while r > l:
                width = r - l
                area = width * min(heights[l], heights[r])
                max_area = max(area, max_area)
                r -= 1
                print(f"area: {area}, max_area: {max_area}, l: {l}, r: {r}, width: {width}, height: {min(heights[l], heights[r])}")
            l += 1
            r = len(heights) - 1
            print("incrementing l")

        return max_area
            