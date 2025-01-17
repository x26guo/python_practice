from typing import Optional, List

from leetcode.TreeNode import TreeNode


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        cur_level = []
        next_level = []
        cur_level.append(root)
        max = root.val
        output = []
        while cur_level:
            cur_node = cur_level.pop()
            if cur_node.val > max:
                max = cur_node.val
            if cur_node.left is not None:
                next_level.append(cur_node.left)
            if cur_node.right is not None:
                next_level.append(cur_node.right)
            if not cur_level:
                output.append(max)
                cur_level = next_level
                next_level = []
                if cur_level:
                    max = cur_level[0].val
        return output