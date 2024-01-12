from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class LinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def __init__(self):
        self.head = LinkedList(0)
        self.curr = self.head

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        def recursion(node):
            if node:
                # do thing
                self.curr.next = LinkedList(node.val)
                self.curr = self.curr.next
                recursion(node.left)
                recursion(node.right)

        recursion(root)

        self.curr = self.head.next
        currTreeNode = root

        while self.curr:

            if currTreeNode.left:
                currTreeNode.left = None
            currTreeNode.val = self.curr.val
            if not currTreeNode.right and self.curr.next:
                currTreeNode.right = TreeNode()
            currTreeNode = currTreeNode.right
            self.curr = self.curr.next

        return
