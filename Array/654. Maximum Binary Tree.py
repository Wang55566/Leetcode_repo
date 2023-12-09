# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def _recursive(sub_list):
            if len(sub_list) == 0:
                return None
            max_n = 0
            idx = 0
            for i in range(len(sub_list)):
                if sub_list[i] > max_n:
                    max_n = sub_list[i]
                    idx = i
            node = TreeNode(max_n)
            left_sublist = sub_list[:idx]
            right_sublist = sub_list[idx+1:]

            node.left = _recursive(left_sublist)
            node.right = _recursive(right_sublist)
            return node


        return _recursive(nums)
