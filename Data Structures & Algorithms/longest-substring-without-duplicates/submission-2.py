class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l, r = 0, 1

        while r <= len(s):
            res = max(res, len(set(s[l:r])))
            while len(set(s[l:r])) < len(s[l:r]):
                l += 1
            r += 1
        return res

