from typing import Optional

from leetcode.TreeNode import TreeNode


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        cur_level = []
        next_level = []
        cur_level.append(root)

        while cur_level:
            cur = cur_level.pop(0)
            if cur.val == val:
                return cur
            if cur.left is not None:
                next_level.append(cur.left)
            if cur.right is not None:
                next_level.append(cur.right)
            if not cur_level:
                cur_level = next_level[:]
                next_level = []
        return None

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

solution = Solution()
solution.searchBST(root, 2)