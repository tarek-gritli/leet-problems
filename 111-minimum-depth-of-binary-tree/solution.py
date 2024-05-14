# Runtime: 247ms, Beats 58.76% of users with Python3
# Memory: 43.64MB, Beats 15.07% of users with Python3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.right:
            return 1+self.minDepth(root.left)
        if not root.left:
            return 1+self.minDepth(root.right)
        return 1+min(self.minDepth(root.right),self.minDepth(root.left))