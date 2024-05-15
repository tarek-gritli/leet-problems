// Runtime: 4ms, Beats 54.89% of users with c++
// Memory: 11.91MB, Beats 5.85% of users with c++

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
    ListNode* reverseList(ListNode* head) {
        if (!head) return nullptr;
        stack<int> st;
        ListNode* current = head;        
        while (current) {
            st.push(current->val);
            current = current->next;
        }        
        ListNode* newHead = new ListNode(st.top());
        st.pop();
        ListNode* curr = newHead;        
        while (!st.empty()) {
            ListNode* newNode = new ListNode(st.top());
            st.pop();
            curr->next = newNode;
            curr = curr->next;
        }
        
        return newHead;

    }
};