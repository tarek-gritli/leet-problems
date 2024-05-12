# Runtime: 371ms, Beats 15.95% of users with Python3
# Memory: 20.04MB, Beats 34.94% of users with Python3

import sys
sys.set_int_max_str_digits(10100)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ch = ""
        dummy = head
        while dummy:
            ch+=str(dummy.val)
            dummy=dummy.next
        ch = str(int(ch)*2)
        new_node = ListNode(int(ch[0]))
        curr = new_node
        for i in range(1,len(ch)):
            node = ListNode(int(ch[i]))
            curr.next = node
            curr = curr.next
        return new_node