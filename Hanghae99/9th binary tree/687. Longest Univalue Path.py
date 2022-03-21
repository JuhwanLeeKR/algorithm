# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional

"""
1. 재귀 함수 사용
2. left가 없을때까지 내려간다 (밑바닥 찍기)
3. 최대 길이 전역 변수 사용
4. value 값을 비교하여 left.val과 현재 val이 같으면 +1
5. 최대 값만 저장
"""


class Solution:
    # 전역 변수 선언
    max_length = 0

    def longestUnivaluePath(self, root: Optional[TreeNode]):  # -> int:
        # root가 없을때 예외처리
        if root is None:
            return 0

        # 함수 선언
        def dfs(node):
            leftLength, rightLength = 0, 0

            if node.left:
                leftLength = dfs(node.left)
                if node.left.val == node.val:
                    leftLength += 1
                else:
                    leftLength = 0

            if node.right:
                rightLength = dfs(node.right)
                if node.right.val == node.val:
                    rightLength += 1
                else:
                    rightLength = 0

            self.max_length = max(self.max_length, leftLength + rightLength)

            return max(leftLength, rightLength)

        dfs(root)
        return self.max_length


sol = Solution()
root = [5, 4, 5, 1, 1, 5]
print(sol.longestUnivaluePath(root))
