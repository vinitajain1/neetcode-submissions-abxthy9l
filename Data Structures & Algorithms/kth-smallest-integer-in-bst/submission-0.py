# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        res = []

        def dfs(root):
            if root:
                left = dfs(root.left)
                if left:
                    res.append(left.val)
                res.append(root.val)
                right = dfs(root.right)
                if right:
                    res.append(right.val)
        dfs(root)
        return res[k-1]