class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        val = root.val

        def recursive(node):
            if node:

                return recursive(node.left) and recursive(node.right) and (node.val == val)

            return True
        return recursive(root)


        # val = root.val

        # def recursive(node):
        #     if node:
        #         print(node.val)
        #         if node.val != val:
        #             return False
        #         elif node.val == val:
        #             return True
        #         else:
        #             recursive(node.left) and recursive(node.right)

        # return recursive(root)
