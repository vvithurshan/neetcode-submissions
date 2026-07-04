# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        

        def dfs(root, maxval):
            nonlocal res

            if root is None:
                return 

            if root.val >= maxval:
                res += 1
                maxval = root.val

            dfs(root.left, maxval)
            dfs(root.right, maxval)

            return

        res  = 0
        dfs(root, float("-inf"))

        return res