# Runtime: 44ms, Beats 76.43% of users with Python3
# Memory: 16.87MB, Beats 49.69% of users with Python3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root.right and not root.left:
            return root.val
        if root.val == 2:
            return self.evaluateTree(root.right) or self.evaluateTree(root.left)
        return self.evaluateTree(root.right) and self.evaluateTree(root.left)