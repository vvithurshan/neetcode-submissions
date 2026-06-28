# June 28

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        res = 0

        def dfs(root):

            nonlocal res

            if root is None:
                return 0

            left = dfs(root.left) # 0
            right = dfs(root.right) # 3 

            res = max(res, left + right) # max(2, 3) = 3

            return 1 + max(left, right) # 1 + 3 = 4 

        dfs(root)

        return res # return 3