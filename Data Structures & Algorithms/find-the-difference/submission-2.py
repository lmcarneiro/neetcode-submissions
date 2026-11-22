class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        h_s = {}
        h_t = {}

        for c in s:
            h_s[c] = 1 + h_s.get(c, 0)
            
        for c in t:
            if c not in h_s:
                return c
            if c in h_s:
                h_s[c] -= 1
                if not h_s[c]:
                    del h_s[c]
        return c