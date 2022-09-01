# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverseReturnSum(self, root: Optional[TreeNode], prev_sum = 0, target = 0) -> int:
        boolResult = False
        if root.left:
            boolResult = self.traverseReturnSum(root.left, prev_sum = prev_sum + root.val, target=target)
        if boolResult:
            return True
        if root.right:
            boolResult = self.traverseReturnSum(root.right, prev_sum = prev_sum + root.val, target = target)
        if boolResult:
            return True
        if not root.left and not root.right:
            prev_sum = prev_sum + root.val
            return prev_sum == target
        return False
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root:
            return self.traverseReturnSum(root, target=targetSum)
        else:
            return False