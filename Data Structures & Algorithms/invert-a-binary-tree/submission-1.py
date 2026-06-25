# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root is None:
            return root

        level = []
        level.append(root)

        while level:
            curr = level.pop()
            left = curr.left
            right = curr.right
            curr.left = right
            curr.right = left

            if right:
                level.append(right)

            if left:
                level.append(left)

        return root 
