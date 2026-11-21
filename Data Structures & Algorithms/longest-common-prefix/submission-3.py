class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        max_word = max(strs)
        for i in range(len(max_word)):
            char = max_word[i]
            for s in strs:
                if i >= len(s) or s[i] != char:
                    return s[:i]
        return max_word