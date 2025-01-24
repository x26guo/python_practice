from typing import Optional, List

from leetcode.ListNode import ListNode


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        num_nodes = 0
        cur = head
        output = []
        while cur is not None:
            cur = cur.next
            num_nodes += 1

        split = num_nodes // k
        remaining = num_nodes % k

        if split == 0:
            cur = head
            while cur is not None:
                next = cur.next
                cur.next = None
                output.append(cur)
                cur = next
                k -= 1
            while k > 0:
                output.append(None)
                k-=1
        else:
            while k > 0:
                rounds = split
                if remaining > 0:
                    rounds += 1
                    remaining -= 1
                cur = head
                while rounds > 1:
                    cur = cur.next
                    rounds -= 1
                next = cur.next
                cur.next = None
                output.append(head)
                head = next
                cur = next
                k -= 1
        return output