# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
#         res1 = ""
#         res2 = ""
#         def recursive(node,res):
#             if not node:
#                 print(res)
#                 return res
#             else:
#                 if not node.left and not node.right:
#                     print("line 17")
#                     res+= str(node.val)
#                 recursive(node.left,res)
#                 recursive(node.right,res)

#         val_res1 = recursive(root1,res1)
#         print("----------")
#         val_res2 = recursive(root1,res2)
#         # print(val_res1, val_res2)
#         if val_res1 == val_res2:
#             return True
#         return False

# class Solution:
#     def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
#         def recursive(node, leaves):
#             if not node:
#                 return leaves
#             else:
#                 if not node.left and not node.right:
#                     leaves.append(node.val)
#                 leaves = recursive(node.left, leaves)
#                 leaves = recursive(node.right, leaves)
#                 return leaves

#         leaves1 = recursive(root1, [])
#         leaves2 = recursive(root2, [])

#         return leaves1 == leaves2

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        root1_leaves = []
        root2_leaves = []
        def dfs(node, rootLeaves):
            if(not node.left and not node.right):
                rootLeaves.append(node.val)
            if(node.left):
                dfs(node.left, rootLeaves)
            if(node.right):
                dfs(node.right, rootLeaves)

        dfs(root1, root1_leaves)
        dfs(root2, root2_leaves)

        return root1_leaves == root2_leaves
