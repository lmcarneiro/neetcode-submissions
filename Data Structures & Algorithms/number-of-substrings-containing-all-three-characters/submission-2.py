class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        res = 0
        last_seen = [-1] * 3

        for i, c in enumerate(s):
            last_seen[ord(c) - 97] = i
            res += min(last_seen) + 1
        return res

                
