class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        h = {} # sorted string: index
        res = []
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s in h:
                res[h[sorted_s]].append(s)
            else:
                res.append([s])
                h[sorted_s] = len(res) - 1
        return res