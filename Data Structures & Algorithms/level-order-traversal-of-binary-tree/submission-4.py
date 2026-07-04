# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []

        def level(root, depth):

            if root is None:
                return

            if depth == len(res):
                res.append([])

            res[depth].append(root.val)
            level(root.left, depth + 1) # I previously used return level()
            level(root.right, depth + 1) # I previously used return level

            # If I use two return, do you think the second recursive call even get 
            # a chance to run

        level(root, 0)

        return res