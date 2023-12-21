from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Iterative solution
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1

        deque1 = deque([root1])
        deque2 = deque([root2])

        while deque1 and deque2:
            node1 = deque1.popleft()
            node2 = deque2.popleft()

            node1.val += node2.val

            if node1.left and node2.left:
                deque1.append(node1.left)
                deque2.append(node2.left)
            elif node2.left:
                node1.left = node2.left

            if node1.right and node2.right:
                deque1.append(node1.right)
                deque2.append(node2.right)
            elif node2.right:
                node1.right = node2.right

        return root1

# recusive solution
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        def merging(node1, node2):
            if not node1 and not node2:
                return None
            elif not node1:
                return node2
            elif not node2:
                return node1
            node1.left = merging(node1.left, node2.left)
            node1.right = merging(node1.right, node2.right)
            node1.val += node2.val
            return node1

        return merging(root1, root2)
