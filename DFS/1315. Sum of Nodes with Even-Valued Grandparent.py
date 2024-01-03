# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        res= 0
        def recursion(current,parent, grandparent):
            nonlocal res
            if not current:
                return
            if grandparent and grandparent.val % 2 == 0:
                res += current.val
            recursion(current.left, current, parent)
            recursion(current.right, current, parent)

        recursion(root,None,None)
        return res
