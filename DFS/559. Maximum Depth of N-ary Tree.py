"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:

    def __init__(self):
        self.level = -1

    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        if not root.children:
            return 1

        def recursion(listNode, level):
            for node in listNode:
                if node.children:
                    recursion(node.children, level + 1)
            self.level = max(self.level, level)


        recursion(root.children, 2)

        return self.level
