"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        h = collections.defaultdict(lambda: Node(0))
        h[None] = None
        node = head

        while node:
            h[node].val = node.val
            h[node].next = h[node.next]
            h[node].random = h[node.random]
            node = node.next

        return h[head]