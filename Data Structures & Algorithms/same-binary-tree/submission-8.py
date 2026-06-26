# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def helper(r1, r2):
            if r1 is None and r2 is None:
                return True

            if r1 is None or r2 is None:
                return False

            return (r1.val == r2.val) and helper(r1.left, r2.left) and \
                    helper(r1.right, r2.right)


        return helper(p, q)