class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        pat_to_s = {}
        s_to_pat = {}

        if len(s) != len(pattern):
            return False

        for i in range(len(s)):
            if s[i] not in s_to_pat and pattern[i] not in pat_to_s:
                s_to_pat[s[i]] = pattern[i]
                pat_to_s[pattern[i]] = s[i]
            elif s[i] in s_to_pat and pattern[i] not in pat_to_s:
                return False
            elif s[i] not in s_to_pat and pattern[i] in pat_to_s:
                return False

        return True