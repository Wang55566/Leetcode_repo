from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        res = float("inf")
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.left:
                current = node.left
                while current.right:
                    current = current.right
                gap = abs(current.val - node.val)
                if gap < res:
                    res = gap
                queue.append(node.left)

            if node.right:
                current = node.right
                while current.left:
                    current = current.left
                gap = abs(current.val - node.val)
                if gap < res:
                    res = gap
                queue.append(node.right)
        return res
