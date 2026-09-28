class Solution:
    def longestPalindrome(self, s: str) -> str:
        res, lenRes = '', 0
        for i in range(len(s)):
            for j in range(i, len(s) + 1):
                if self.isPalindrome(s[i:j]):
                    if len(s[i:j]) > lenRes:
                        res = s[i:j]
                        lenRes = len(s[i:j])
        return res
        
    def isPalindrome(self, sub):
        l, r = 0, len(sub) - 1
        while l < r:
            if sub[l] != sub[r]:
                return False
            l += 1
            r -= 1
        return True