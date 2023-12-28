# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nums = []

        if not root:
            return nums

        def recursion(node):
            nonlocal nums
            if node.left:
                recursion(node.left)
            nums.append(node.val)
            if node.right:
                recursion(node.right)

        recursion(root)
        return nums
