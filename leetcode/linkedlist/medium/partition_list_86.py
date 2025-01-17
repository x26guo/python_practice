from typing import Optional

from leetcode.ListNode import ListNode


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left_head = ListNode(-1)
        left_cur = left_head
        right_head = ListNode(-1)
        right_cur = right_head

        cur = head
        while cur is not None:
            if cur.val < x:
                left_cur.next = ListNode(cur.val)
                left_cur = left_cur.next
            else:
                right_cur.next = ListNode(cur.val)
                right_cur = right_cur.next
            cur = cur.next
        left_cur.next = right_head.next
        return left_head.next