# June 28

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        level = deque()
        level.append((p, q))

        while level:
            t1, t2 = level.popleft()

            if t1 is None and t2 is None:
                continue

            if t1 is None or t2 is None:
                return False

            if t1.val != t2.val:
                return False

            level.append((t1.left, t2.left))
            level.append((t1.right, t2.right))

        return True
            