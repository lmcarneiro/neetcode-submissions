class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        h = defaultdict(list)

        for s in strs:
            word = [0] * 26
            for char in s:
                word[ord(char) - ord("a")] += 1

            h[tuple(word)].append(s)

        return list(h.values())