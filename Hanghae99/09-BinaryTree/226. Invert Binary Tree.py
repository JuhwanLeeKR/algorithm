# https://leetcode.com/problems/invert-binary-tree/

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]):  # -> Optional[TreeNode]:
        # 예외처리
        if root is None:
            return
        right = self.invertTree(root.right)
        left = self.invertTree(root.left)

        root.left = right
        root.right = left
        return root


root = [4, 2, 7, 1, 3, 6, 9]

node6 = TreeNode(root[6], None, None)
node5 = TreeNode(root[5], None, None)
node4 = TreeNode(root[4], None, None)
node3 = TreeNode(root[3], None, None)
node2 = TreeNode(root[2], node5, node6)
node1 = TreeNode(root[1], node3, node4)
node0 = TreeNode(root[0], node1, node2)

sol = Solution()
print(sol.invertTree(node0))
