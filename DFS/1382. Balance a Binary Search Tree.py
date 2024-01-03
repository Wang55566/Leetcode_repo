# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        listNum = []

        def recursion(node):
            if not node:
                return
            recursion(node.left)
            recursion(node.right)
            listNum.append(node.val)

        recursion(root)
        listNum.sort()

        def buildBST(nums):
            if len(nums) == 0:
                return
            middle = len(nums)//2
            newNode = TreeNode(nums[middle])
            newNode.left = buildBST(nums[:middle])
            newNode.right = buildBST(nums[middle + 1:])
            return newNode

        return buildBST(listNum)
