# Runtime: 38ms, Beats 37.48% of users with Python3
# Memory: 16.57MB, Beats 34.33% of users with Python3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        root.right, root.left = root.left, root.right
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
        