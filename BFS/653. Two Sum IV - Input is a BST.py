class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import Optional

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        queue = deque([root])

        while queue:
            node = queue.popleft()
            target = k - node.val

            # place children into queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

            if target == node.val:
                continue


            # treverse BST to find the target
            current = root
            while current:
                if current.val > target:
                    current = current.left
                elif current.val < target:
                    current = current.right
                elif current.val == target:
                    return True

        return False
