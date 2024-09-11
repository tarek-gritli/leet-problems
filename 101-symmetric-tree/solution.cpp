// Runtime: 3ms, Beats 70.22% of users with C++
// Memory: 17.39MB, Beats 37.62% of users with C++

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
    bool isSymmetric(TreeNode* root) {
        if (root == nullptr) {
            return true;
        }
        return compare(root->left,root->right);
    }
    bool compare(TreeNode* n1, TreeNode* n2) {
        if (n1 == nullptr && n2 == nullptr) return true;
        if (n1==nullptr || n2==nullptr) return false;
        return n1->val == n2->val && compare(n1->right,n2->left) && compare(n1->left,n2->right);
    }
};