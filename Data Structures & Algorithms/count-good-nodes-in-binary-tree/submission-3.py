# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        if root is None:
            return 0

        dq = deque()
        dq.append((root, float("-inf")))
        res = 0

        while dq:

            node, maxval = dq.popleft()

            if node.val >= maxval:
                res += 1
                maxval = node.val

            if node.left:
                dq.append((node.left, maxval))

            if node.right:
                dq.append((node.right, maxval))

        return res