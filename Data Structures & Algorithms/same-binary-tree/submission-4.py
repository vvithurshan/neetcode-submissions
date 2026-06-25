# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if p is None and q is None:
            return True

        if p is None or q is None:
            return False 

        s1 = deque()
        s2 = deque()

        s1.append(p)
        s2.append(q)

        while s1 and s2:

            if len(s1) != len(s2):
                return False

            for _ in range(len(s1)):
                
                node1 = s1.popleft()
                node2 = s2.popleft()

                if node1 is None and node2 is None:
                    continue

                if node1 is None or node2 is None:
                    return False

                if node1.val != node2.val:
                    return False

                
                if node1.left or node2.left:
                    if node1.left and node2.left:
                        s1.append(node1.left)
                        s2.append(node2.left)

                    else:
                        return False

                if node1.right or node2.right:
                    if node1.right and node2.right:
                        s1.append(node1.right)
                        s2.append(node2.right)

                    else:
                        return False

        return not (s1 or s2)