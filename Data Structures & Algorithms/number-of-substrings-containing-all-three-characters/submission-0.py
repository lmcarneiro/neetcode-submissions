class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        res = 0
        window = [-1] * 3

        for i, c in enumerate(s):
            window[ord(c) - 97] = i
            res += min(window) + 1
        return res

                
