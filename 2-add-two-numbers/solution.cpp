// Runtime: 19ms, Beats 76.09% of users with C++
// Memory: 76.15MB, Beats 8.52% of users with C++

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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int carry=0;
        ListNode* res=new ListNode();
        ListNode* head=res;
        int x,y,val;
        while(l1 || l2 || carry)
        {   
            x=l1 ? l1->val : 0;
            y=l2 ? l2->val : 0;
            val=x+y+carry;
            if(val>=10)
            {
                val-=10;
                carry=1;
            }
            else carry=0;
            res->next=new ListNode(val);
            res=res->next;
            l1=l1? l1->next: NULL;
            l2=l2? l2->next: NULL;
        }
        return head->next;
    }
};