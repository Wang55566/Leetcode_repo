# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.counter = 0

    def goodNodes(self, root: TreeNode) -> int:
        def recursion(node,maximum):
            if node:
                if node.val >= maximum:
                    self.counter +=1
                    maximum = node.val
                recursion(node.left,maximum)
                recursion(node.right,maximum)


        recursion(root,root.val)
        return self.counter
