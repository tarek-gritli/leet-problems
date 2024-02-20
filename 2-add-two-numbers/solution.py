# Runtime: 54ms, Beats 68.05% of users with Python3
# Memory: 16.54MB, Beats 95.14% of users with Python3

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res=ListNode()
        head=res
        carry=0
        while l1 or l2 or carry:
            x=l1.val if l1 else 0
            y=l2.val if l2 else 0
            val=x+y+carry
            if x+y+carry>=10:
                val-=10
                carry=1
            else:
                carry=0
            res.next=ListNode(val)
            res=res.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        return head.next           