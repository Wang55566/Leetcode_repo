from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        while queue:
            sum = 0
            for i in range(len(queue)):
                parent_node = queue.popleft()
                sum += parent_node.val
                if parent_node.left:
                    queue.append(parent_node.left)
                if parent_node.right:
                    queue.append(parent_node.right)
        return sum
