# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if root is None:
            return []
        
        level = deque()
        
        level.append(root)

        res = []

        levelIdx = 0

        while level:
            
            for _ in range(len(level)):

                node = level.popleft()

                if levelIdx == len(res):
                    res.append(node.val)

                if node.right:
                    level.append(node.right)

                if node.left:
                    level.append(node.left)

            levelIdx += 1

        return res


