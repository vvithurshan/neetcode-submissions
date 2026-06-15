# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxsofar):

            if node is None:
                return 0

            res = 1 if node.val >= maxsofar else 0
            maxsofar = max(maxsofar, node.val)
            res += dfs(node.left, maxsofar)
            res += dfs(node.right, maxsofar)
            return res

        return dfs(root, -float('inf'))