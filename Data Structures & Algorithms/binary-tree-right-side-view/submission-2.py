# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        res = []
        q = deque()
        q.append(root)

        while q:
            rightSide = None

            for _ in range(len(q)):
                curr = q.popleft()

                if curr:
                    q.append(curr.left)
                    q.append(curr.right)
                    rightSide = curr

            if rightSide:
                res.append(rightSide.val)
        return res