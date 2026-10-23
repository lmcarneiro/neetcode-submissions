class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = {node: [] for node in range(n)}
        visit = set()

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        res = 0
        def dfs(node):
            if node in visit:
                return False

            visit.add(node)
            for nei in adj[node]:
                dfs(nei)
            
            return True

        for node in range(n):
            if dfs(node):
                res += 1
        
        return res