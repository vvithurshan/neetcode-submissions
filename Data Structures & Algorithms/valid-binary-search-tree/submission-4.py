# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        if root is None: 
            return True # I did not not what to put here

        level = deque()

        level.append((root, float("-inf"), float("inf")))

        while level:
            node, left, right = level.popleft()

            if not (left < node.val < right):
                return False

            if node.left:
                level.append((node.left, left, node.val))

            if node.right:
                level.append((node.right, node.val, right))

        return True

