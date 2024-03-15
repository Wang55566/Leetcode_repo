# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if not root:
            root = TreeNode(val)
            return root

        def recursion(node):
            if val > node.val:
                if node.right:
                    recursion(node.right)
                else:
                    node.right = TreeNode(val)
                    return
            else:
                if node.left:
                    recursion(node.left)
                else:
                    node.left = TreeNode(val)
                    return

        recursion(root)
        return root
