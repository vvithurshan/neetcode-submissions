# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(root1, root2):

            if root1 is None and root2 is None:
                return True

            if root1 is None or root2 is None:
                return False

            return (root1.val == root2.val) and \
                    dfs(root1.left, root2.left) and \
                    dfs(root1.right, root2.right)


        q = deque()
        q.append(root)

        while q:
            node = q.popleft()
            if dfs(node, subRoot):
                return True

            if node.left:
                q.append(node.left)
            
            if node.right:
                q.append(node.right)

        return False