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
        
        h = {None: None}
        node = head

        while node:
            new_node = Node(node.val)
            h[node] = new_node
            node = node.next


        node = head

        while node:
            copy = h[node]
            copy.next = h[node.next]
            copy.random = h[node.random]
            node = node.next

        return h[head]