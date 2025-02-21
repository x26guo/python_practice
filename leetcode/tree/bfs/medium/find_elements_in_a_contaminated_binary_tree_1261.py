from typing import Optional

from leetcode.TreeNode import TreeNode


class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.dic = {}
        cur_level = []
        next_level = []

        root.val = 0
        cur_level.append(root)
        self.dic[root.val] = root.val

        while cur_level:
            current = cur_level.pop(0)
            if current.left is not None:
                current.left.val = current.val * 2 + 1
                next_level.append(current.left)
                self.dic[current.left.val] = current.left.val
            if current.right is not None:
                current.right.val = current.val * 2 + 2
                next_level.append(current.right)
                self.dic[current.right.val] = current.right.val
            if not cur_level:
                cur_level = next_level
                next_level = []

    def find(self, target: int) -> bool:
        return target in self.dic