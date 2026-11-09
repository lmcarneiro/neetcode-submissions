# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, s):
            if not root:
                return False

            s += root.val
            if not root.left and not root.right:
                return s == targetSum
            
            if dfs(root.left, s):
                return True
            if dfs(root.right, s):
                return True
            s -= root.val
            return False

        return dfs(root, 0)
            