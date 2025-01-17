from typing import Optional

from leetcode.ListNode import ListNode


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None or head.next.next is None:
            return head
        num_of_nodes = 1
        cur = head
        while cur.next is not None:
            num_of_nodes = num_of_nodes + 1
            cur = cur.next
        end = cur
        cur = head
        for i in range(num_of_nodes // 2):
            moved = cur.next
            cur.next = cur.next.next
            moved.next = None
            end.next = moved
            end = end.next
            cur = cur.next
        return head