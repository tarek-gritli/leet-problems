# Runtime: 39ms, Beats 72.14% of users with Python3
# Memory: 17.38MB, Beats 87.57% of users with Python3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.right and not root.left:
            return root.val == targetSum
        a = self.hasPathSum(root.right,targetSum-root.val)
        b = self.hasPathSum(root.left,targetSum-root.val)
        return a or b
            

