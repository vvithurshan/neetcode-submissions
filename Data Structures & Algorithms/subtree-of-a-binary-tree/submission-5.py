# June 28

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if root is None:
            return False

        if subRoot is None:
            return True

        if self.isSameTree(root, subRoot):
            return True


        return self.isSubtree(root.left, subRoot) or \
                self.isSubtree(root.right, subRoot)
    
    def isSameTree(self, root, sub):
        
        if root is None and sub is None:
            return True

        if root is None or sub is None:
            return False

        if root.val == sub.val:
            return self.isSameTree(root.left, sub.left) and \
                self.isSameTree(root.right, sub.right)

        else:
            return False