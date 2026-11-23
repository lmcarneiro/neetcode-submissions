class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        count = defaultdict(int)
        res = set()
        if len(s) <= 10:
            return []

        for i in range(len(s) - 9):
            sub = s[i:i+10]
            count[sub] += 1
            if count[sub] > 1:
                res.add(sub)
        
        return list(res)