class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

        def recursion(currNode, parentNode, direction):
            if currNode:
                currNode.left = recursion(currNode.left, currNode, "left")
                currNode.right = recursion(currNode.right,currNode, "right")
                if currNode.val == target and not currNode.left and not currNode.right:
                    if not parentNode:
                        return None
                    if direction == "left":
                        parentNode.left = None
                    else:
                        parentNode.right = None
                    return

            return currNode
