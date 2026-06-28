# June 28

from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return 0

        level = deque()
        level.append(root)

        depth = 0 

        while level:
            for _ in range(len(level)):
                node = level.popleft()

                if node.left:
                    level.append(node.left)

                if node.right:
                    level.append(node.right)

            depth += 1

        return depth