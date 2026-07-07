"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if node is None:
            return 
        
        oldnew = {}

        def bfs(node):

            dq = deque()

            dq.append(node)

            oldnew[node] = Node(node.val)

            while dq:
                cur = dq.popleft()

                for neh in cur.neighbors:
                    if neh not in oldnew:
                        oldnew[neh] = Node(neh.val)
                        dq.append(neh)

                    oldnew[cur].neighbors.append(oldnew[neh])

            
            return oldnew[node]

        return bfs(node)