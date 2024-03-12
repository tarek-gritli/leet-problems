# Runtime: 65ms, Beats 14.23% of users with Python3
# Memory: 16.75MB, Beats 89.33% of users with Python3


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        front = ListNode(0,head)
        start = front
        while start:
            pref=0
            end=start.next
            while end:
                pref+=end.val
                if pref == 0:
                    start.next = end.next
                end = end.next
            start = start.next
        return front.next
            
            


