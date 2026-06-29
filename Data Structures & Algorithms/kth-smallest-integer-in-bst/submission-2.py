# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []

        def dfs(root):
            if root is None:
                return root

            left = dfs(root.left)
            right = dfs(root.right)

            heapq.heappush(res, -root.val)

            if len(res) > k:
                heapq.heappop(res)

        dfs(root)

        return -heapq.heappop(res)