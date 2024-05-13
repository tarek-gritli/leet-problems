// Runtime: 0ms, Beats 100.00% of users with Python3
// Memory: 11.39MB, Beats 51.44% of users with Python3

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if (root == nullptr) return nullptr;
        invertTree(root->left);
        invertTree(root->right);
        TreeNode* temp = root->right;
        root->right = root->left;
        root->left = temp;
        return root;
    }
};
        