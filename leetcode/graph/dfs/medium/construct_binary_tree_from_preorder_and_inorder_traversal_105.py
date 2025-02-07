from typing import List, Optional

from leetcode.TreeNode import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if preorder is None or len(preorder) == 0:
            return None
        root_val = preorder[0]
        rootNode = TreeNode(root_val)
        inorder_index = inorder.index(root_val)
        left_inorder = inorder[0:inorder_index]
        right_inorder = inorder[inorder_index + 1:]

        left_preorder = preorder[1:1+inorder_index]
        right_preorder = preorder[1+inorder_index:]

        rootNode.left = self.buildTree(left_preorder, left_inorder)
        rootNode.right = self.buildTree(right_preorder, right_inorder)

        return rootNode

solution = Solution()
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
solution.buildTree(preorder, inorder)