"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        clones = {}

        def dfs(n):
            if n.val not in clones:
                clones[n.val] = Node(n.val)
                for neighbor in n.neighbors:
                    clones[n.val].neighbors.append(dfs(neighbor))
            
            return clones[n.val]
        
        return dfs(node) if node else None