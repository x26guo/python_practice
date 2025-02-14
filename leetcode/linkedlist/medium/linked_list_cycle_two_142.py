from typing import Optional

from leetcode.ListNode import ListNode


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        dic = {}
        while cur is not None and cur.next is not None:
            if cur.next in dic:
                return dic[cur.next]
            dic[cur.next] = cur.next
            cur = cur.next
        return None