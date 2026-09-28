class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 1
        max_len = 0
        while j <= len(s):
            max_len = max(max_len, len(set(s[i:j])))
            while len(set(s[i:j])) < len(s[i:j]):
                i += 1
            j += 1

        return max_len

