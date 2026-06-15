# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if root is None and subRoot is None:
            return True

        def isSub(main, sub):
            if main is None and sub is None:
                return True
            if main is None or sub is None:
                return False
            
            if main.val == sub.val:  
                return isSub(main.left, sub.left) and isSub(main.right, sub.right)
            else:
                return False

        q = deque()
        q.append(root)

        while q:
            curr = q.popleft()

            if curr and curr.val == subRoot.val:
                if isSub(curr, subRoot): 
                    return True

            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)

        return False

                

