// Runtime: 0ms, Beats 100.00% of users with C++
// Memory: 8.59MB, Beats 66.29% of users with C++

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
class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        int n=0;
        ListNode *dummy = head;
        while(dummy)
        {
            n++;
            dummy = dummy->next;
        }
        dummy = head;
        for (int i=0;i<n/2;i++)
        {
            dummy = dummy->next;
        }
        return dummy;
    }
};