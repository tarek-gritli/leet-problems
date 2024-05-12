# Runtime: 218ms, Beats 88.97% of users with Python3
# Memory: 19.40MB, Beats 58.37% of users with Python3

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr:
            x = curr.val * 2
            if x < 10:
                curr.val = x 
            elif prev:
                curr.val = x%10
                prev.val +=1
            else:
                new_head = ListNode(1)
                new_head.next = head
                head = new_head
                curr.val = x%10
            prev = curr
            curr = curr.next
        return head