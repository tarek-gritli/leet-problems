// Runtime: 8ms, Beats 98.28% of users with C++
// Memory: 29.01MB, Beats 72.79% of users with C++


/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
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
    TreeNode* sortedListToBST(ListNode* head) {
        if(head == NULL) return NULL;

        ListNode* mid = findMiddle(head);
        TreeNode* root = new TreeNode(mid->val);

        if(head == mid) return root;

        root->left = sortedListToBST(head);
        root->right = sortedListToBST(mid->next);
        return root;
    }
private:
    ListNode* findMiddle(ListNode* head) {
        ListNode* fast = head;
        ListNode* slow = head;
        ListNode* prev = NULL;

        while(fast && fast->next != NULL) {
            prev = slow;
            slow = slow->next;
            fast = fast->next->next;
        }
        if(prev!=NULL) {
            prev->next = NULL;
        }
        return slow;
    }
};