class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        l = 0
        s = [0] * 26
        t = [0] * 26

        for i in range(len(s1)):
            t[ord(s1[i]) - ord("a")] += 1
            s[ord(s2[i]) - ord("a")] += 1
        
        if s == t:
            return True

        for r in range(len(s1), len(s2)):
            s[ord(s2[l]) - ord("a")] -= 1
            s[ord(s2[r]) - ord("a")] += 1
            l += 1
            if s == t:
                return True
        
        return False