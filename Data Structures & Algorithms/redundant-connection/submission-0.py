class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = {i: [] for i in range(n + 1)}

        def dfs(node, prev):
            if seen[node]:
                return True
            
            seen[node] = True
            for nei in adj[node]:
                if nei == prev:
                    continue
                if dfs(nei, node):
                    return True
            return False
            
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
            seen = [False] * (n + 1)
            if dfs(n1, -1):
                return [n1, n2]
        return []
