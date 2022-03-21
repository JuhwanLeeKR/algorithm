# https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    # 전역 변수 처리
    max_length = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]):  # -> int:
        # root 값이 없을때 예외 처리
        if root is None:
            return 0

        # 재귀함수 사용을 위한 함수 선언
        def dfs(node):
            left_length = 0
            right_length = 0

            # 현재 node의 left 값이 있다면
            if node.left:
                # left_length의 길이에 1을 추가해 줍니다.
                left_length = dfs(node.left) + 1
            if node.right:
                right_length = dfs(node.right) + 1
            self.max_length = max(self.max_length, left_length + right_length)

            return max(left_length, right_length)

        dfs(root)
        return self.max_length


sol = Solution()

root = [1, 2, 3, 4, 5]

print(sol.diameterOfBinaryTree(root))
