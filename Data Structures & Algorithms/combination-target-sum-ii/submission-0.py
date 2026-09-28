class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        s = []
        candidates.sort()

        def dfs(i):
            if sum(s) == target:
                if s not in res:
                    res.append(s.copy())
                return
            if i >= len(candidates):
                return
            
            s.append(candidates[i])
            dfs(i + 1)
            s.pop()
            dfs(i + 1)

        dfs(0)
        return res