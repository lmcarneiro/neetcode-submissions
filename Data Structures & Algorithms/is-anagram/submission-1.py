class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hs, ht = {}, {}
        for i in range(len(s)):
            if s[i] in hs:
                hs[s[i]] += 1
            else:
                hs[s[i]] = 1
            if t[i] in ht:
                ht[t[i]] += 1
            else:
                ht[t[i]] = 1
        return hs == ht
