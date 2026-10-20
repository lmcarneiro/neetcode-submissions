class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        pre_map = {course: [] for course in range(numCourses)}

        for crs, pre in prerequisites:
            pre_map[crs].append(pre)

        def dfs(crs):
            if crs in visited:
                return False
            if not pre_map[crs]:
                return True
            visited.add(crs)
            for pre in pre_map[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            pre_map[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True