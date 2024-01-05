from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:

        def recursion(list):

            if len(list) == 0:
                return None
            node = TreeNode(list[0])
            node.left = recursion([x for x in list if x < list[0]])
            node.right = recursion([x for x in list if x > list[0]])


            return node

        return recursion(preorder)
