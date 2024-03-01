from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.existed = None

    def find(self, target: int) -> bool:
        self.existed = False
        def recursion(value, node):
            if value == target:
                self.existed = True
                return
            if node.left:
                recursion(2*value + 1, node.left)
            if node.right:
                recursion(2*value + 2, node.right)

        recursion(0, self.root)
        return self.existed




# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
