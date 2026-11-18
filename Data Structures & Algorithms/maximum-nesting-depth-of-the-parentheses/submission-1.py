class Solution:
    def maxDepth(self, s: str) -> int:
        cur_lvl = max_lvl = 0
        for c in s:
            if c == "(":
                cur_lvl += 1
                max_lvl = max(cur_lvl, max_lvl)
            elif c == ")":
                cur_lvl -= 1
            
        return max_lvl