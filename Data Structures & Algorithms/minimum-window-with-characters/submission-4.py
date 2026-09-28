class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        if t == s:
            return s
        if t == "":
            return ""

        l = 0
        countS = {}
        countT = {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        have = 0
        need = len(countT)
        res = [-1, -1]
        resLen = float("inf")

        
        
        for r in range(len(s)):
            c = s[r]
            countS[c] = 1 + countS.get(c, 0)

            if c in countT and countS[c] == countT[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                countS[s[l]] -= 1
                if s[l] in countT and countS[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        if resLen != float("inf"):
            return s[l:r+1]
        else:
            return ""


