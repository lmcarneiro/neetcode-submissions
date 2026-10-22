class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        pre_map = {crs: [] for crs in range(numCourses)}
        visit = set()

        for crs, pre in prerequisites:
            pre_map[crs].append(pre)

        def dfs(crs, res):
            if crs in visit:
                return False
            if not pre_map[crs]:
                return True
            visit.add(crs)
            for pre in pre_map[crs]:
                if not dfs(pre, res):
                    return False
                if pre not in res:
                    res.append(pre)
            pre_map[crs] = []
            visit.remove(crs)
            return True
        
        for crs in range(numCourses):
            if dfs(crs, res):
                if crs not in res:
                    res.append(crs)
        
        return res if len(res) == numCourses else []