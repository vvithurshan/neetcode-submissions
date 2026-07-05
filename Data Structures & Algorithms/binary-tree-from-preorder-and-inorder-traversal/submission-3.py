# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        self.pre = 0 
        Index = {}

        for id, val in enumerate(inorder):
            Index[val] = id

        def construct(l, r):
            if r < l:
                return None

            root_val = preorder[self.pre]
            self.pre += 1

            loc = Index[root_val]
            
            root = TreeNode(root_val)

            root.left = construct(l, loc - 1)

            root.right = construct(loc + 1, r)

            return root

        return construct(0, len(inorder) - 1)