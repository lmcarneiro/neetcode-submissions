class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        ana = defaultdict(list)

        for s in strs:
            word = [0] * 26
            for c in s:
                word[ord(c) - ord("a")] += 1
            ana[tuple(word)].append(s)

        return list(ana.values())