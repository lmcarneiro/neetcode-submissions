# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_q = deque()
        q_q = deque()

        p_q.append(p)
        q_q.append(q)

        while p_q and q_q:
            for i in range(len(p_q)):
                nodeP = p_q.popleft()
                nodeQ = q_q.popleft()

                if nodeP is None and nodeQ is None:
                    continue
                if nodeP is None or nodeQ is None or nodeP.val != nodeQ.val:
                    return False

                p_q.append(nodeP.left)
                p_q.append(nodeP.right)
                q_q.append(nodeQ.left)
                q_q.append(nodeQ.right)

        return True