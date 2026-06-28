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

        maxSofar = -200

        level =  deque()

        level.append((root, maxSofar))
        res = 0

        while level:

            for _ in range(len(level)):

                node, maxSofar = level.popleft()

                if node.val >= maxSofar:
                    res += 1
                    maxSofar = node.val

                if node.left:
                    level.append((node.left, maxSofar))

                if node.right:
                    level.append((node.right, maxSofar))

        return res
