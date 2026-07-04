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

        level = 0 

        res = []
         
        dq = deque()
        dq.append((root, level))

        while dq:

            for _ in range(len(dq)):

                node, curLevel = dq.popleft()

                if curLevel == level:
                    res.append(node.val)
                    level += 1

                if node.right:
                    dq.append((node.right, curLevel + 1))

                if node.left:
                    dq.append((node.left, curLevel + 1))


        return res