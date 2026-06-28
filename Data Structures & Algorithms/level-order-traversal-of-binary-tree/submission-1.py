# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return []
            
        level = deque()

        level.append(root)
        res = []

        while level:
            sub = []

            for _ in range(len(level)):

                node = level.popleft()

                sub.append(node.val)

                if node.left:
                    level.append(node.left)

                if node.right:
                    level.append(node.right)

            res.append(sub)

        return res

