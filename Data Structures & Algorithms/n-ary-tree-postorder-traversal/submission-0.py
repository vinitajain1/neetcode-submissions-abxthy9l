"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        def postorderntree(node):
            if node:
                for n in node.children:
                    postorderntree(n)
                res.append(node.val)
        postorderntree(root)
        return res