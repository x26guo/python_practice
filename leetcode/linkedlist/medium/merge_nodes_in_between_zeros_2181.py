# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from leetcode.ListNode import ListNode


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head_output = ListNode(-1)
        output_cur = head_output

        cur = head
        sum = 0
        while cur is not None:
            if cur.val == 0:
                if sum != 0:
                    output_cur.next = ListNode(sum)
                    output_cur = output_cur.next
                    sum = 0
            else:
                sum += cur.val
            cur = cur.next
        return head_output.next