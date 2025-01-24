from typing import Optional

from leetcode.ListNode import ListNode


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def get_middle_index(head: ListNode) -> int:
            i = 1
            cur = head
            while cur.next is not None:
                i += 1
                cur = cur.next
            return i // 2

        def merge(left_node: ListNode, right_node: ListNode) -> ListNode:
            dummy = ListNode(-1)
            cur = dummy
            while left_node is not None and right_node is not None:
                if left_node.val <= right_node.val:
                    cur.next = left_node
                    left_node = left_node.next
                else:
                    cur.next = right_node
                    right_node = right_node.next
                cur = cur.next

            if left_node is not None:
                cur.next = left_node
            if right_node is not None:
                cur.next = right_node
            return dummy.next


        if head is None or head.next is None:
            return head

        middle = head
        for i in range(1, get_middle_index(head)):
            middle = middle.next

        right = middle.next
        middle.next = None

        left = self.sortList(head)
        right = self.sortList(right)

        result = merge(left, right)
        return result

solution = Solution()
head = ListNode(4)
head.next = ListNode(2)
head.next.next = ListNode(1)
head.next.next.next = ListNode(3)

solution.sortList(head)