from typing import Optional, List

from leetcode.ListNode import ListNode


class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dic = {}
        for n in nums:
            if n not in dic:
                dic[n] = 1

        pre_head = ListNode(-1)
        pre_head.next = head
        pre = pre_head
        cur = head

        while cur is not None:
            if cur.val in dic:
                cur = cur.next
                pre.next = cur
            else:
                pre = cur
                cur = cur.next

        return pre_head.next