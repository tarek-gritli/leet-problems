# Runtime: 43ms, Beats 47.83% of users with Python3
# Memory: 18.37MB, Beats 48.68% of users with Python3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    INF = float('inf')
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(node,mini, maxi):
            if not node:
                return True
            if node.val>=maxi or node.val<=mini:
                return False
            return isValid(node.left,mini,node.val) and isValid(node.right,node.val, maxi)
            
        return isValid(root,-self.INF,self.INF)