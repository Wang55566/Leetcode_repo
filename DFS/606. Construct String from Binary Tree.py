from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:

        res = ""

        if root:
            res += str(root.val)

        def dfs(node):
            if node:
                nonlocal res
                res += '(' + str(node.val)
                if not node.left and node.right:
                    res += '()'
                dfs(node.left)
                dfs(node.right)
                res += ')'


        if not root.left and root.right:
            res += '()'
        dfs(root.left)
        dfs(root.right)

        return res
