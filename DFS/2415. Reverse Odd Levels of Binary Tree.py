class Solution:

    def __init__(self):
        self.templist = []

    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root.left:
            return root

        def recursion(node1, node2, boolean):

            if node1 and node2:
                if boolean:
                    node1.val, node2.val = node2.val, node1.val
                recursion(node1.left, node2.right, not boolean)
                recursion(node1.right, node2.left, not boolean)

        recursion(root.left, root.right, True)

        return root
