# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if root is None:
            return True

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        if abs(left - right) > 1:
            return False
        
        return self.isBalanced(root.left) and \
        self.isBalanced(root.right)
        
    def dfs(self, node):
        if node is None:
            return 0

        left = self.dfs(node.left)
        right = self.dfs(node.right)

        return max(left, right) + 1
