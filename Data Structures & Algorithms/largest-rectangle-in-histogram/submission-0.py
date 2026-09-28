class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        res = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                stack_i, stack_h = stack.pop()
                res = max(res, stack_h * (i - stack_i))
                start = stack_i
            stack.append((start, h))
        
        for i, h in stack:
            res = max(res, h * (len(heights) - i))
        return res            
            