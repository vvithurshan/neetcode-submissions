# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.cnt = k
        self.res = None

        def dfs(root):
            
            if root is None:
                return

            dfs(root.left)

            if self.cnt == 0:
                return 

            self.cnt -= 1 # I am forgetting to add 1 here
            # Remember, you cannot access the variable k here

            if self.cnt == 0:
                self.res = root.val
                return 

            dfs(root.right)

        dfs(root) 

        return self.res