# July 4

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        dq = deque()
        dq.append((p, q))

        while dq:
            root1, root2 = dq.popleft()

            if root1 is None and root2 is None:
                continue

            if root1 is None or root2 is None:
                return False

            if root1.val != root2.val:
                return False

            dq.append((root1.left, root2.left))
            dq.append((root1.right, root2.right))

            # if root1.left and root2.left:
            #     q.apend((root1.left, root2.left))

            # ir root1.left or root2.

        return True