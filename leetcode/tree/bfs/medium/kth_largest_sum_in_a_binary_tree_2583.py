import heapq
from typing import Optional

from leetcode.TreeNode import TreeNode


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        output = []
        cur_level = []
        next_level = []
        cur_level.append(root)
        sum = 0
        max_val = root.val
        while cur_level:
            current = cur_level.pop()
            sum += current.val
            if current.left is not None:
                next_level.append(current.left)
            if current.right is not None:
                next_level.append(current.right)
            if not cur_level:
                if sum:
                    heapq.heappush(output, -sum)
                cur_level = next_level
                next_level = []
                sum = 0
        while k > 0:
            max_val = heapq.heappop(output)
            k -= 1
            if not output:
                break
        if k > 0: return -1
        return -max_val

solution = Solution()
root = TreeNode(605481)
root.right = TreeNode(87336)
root.right.right = TreeNode(226750)
solution.kthLargestLevelSum(root, 1)