class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        visit = set()
        adj = {node: [] for node in range(n)}
        
        for node, edge in edges:
            adj[node].append(edge)
            adj[edge].append(node)

        def dfs(node, prev):
            if node in visit:
                return False

            visit.add(node)
            for edge in adj[node]:
                if edge == prev:
                    continue
                print("node, edge", node, edge, adj[node], visit)
                if not dfs(edge, node):
                    return False

            return True
        
        
        return dfs(0, -1) and len(visit) == n