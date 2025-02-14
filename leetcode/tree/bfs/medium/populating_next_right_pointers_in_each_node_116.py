from typing import Optional


class Solution:

    class Node:
        def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
            self.val = val
            self.left = left
            self.right = right
            self.next = next

    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None

        cur_level = []
        next_level = []
        cur_level.append(root)
        root.next = None

        while cur_level:
            cur = cur_level.pop(0)
            if cur.left is not None:
                next_level.append(cur.left)
            if cur.right is not None:
                next_level.append(cur.right)

            if not cur_level:
                if next_level:
                    for i in range(len(next_level)):
                        if i == len(next_level) - 1:
                            next_level[i].next = None
                            break
                        next_level[i].next = next_level[i+1]
                cur_level = next_level
                next_level = []
        return root

