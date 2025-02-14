from typing import Optional

from leetcode.ListNode import ListNode


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        pre = ListNode(-1)
        cur = head
        head = head.next
        while cur is not None and cur.next is not None:
           next_next = cur.next.next
           cur_next = cur.next
           pre.next = cur_next
           cur_next.next = cur
           cur.next = next_next
           pre = cur
           cur = next_next


        return head

solution = Solution()
root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
root.next.next.next = ListNode(4)

solution.swapPairs(root)
