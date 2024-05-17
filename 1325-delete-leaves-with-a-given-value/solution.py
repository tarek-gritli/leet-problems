#Runtime: 43ms, Beats 75.33% of users with Python3
# Memory: 17.10MB, Beats 28.92% of users with Python3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root:
            return None
        root.left = self.removeLeafNodes(root.left,target)
        root.right = self.removeLeafNodes(root.right,target)
        if not root.right and not root.left and root.val == target:
            return None
        else:
            return root