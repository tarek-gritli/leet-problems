// Runtime: 2ms, Beats 87.52% of users with C
// Memory: 8.06MB, Beats 26.58% of users with C

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int maxDepth(struct TreeNode* root) {
    if(!root) return 0;
    return 1+fmax(maxDepth(root->right),maxDepth(root->left));
}