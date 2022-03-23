# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional

"""
1. 트리구조이고 그래프이니깐 dfs를 사용하자
2. left가 없을때까지 내려간다 (밑바닥 찍기)
3. 최대 길이 전역 변수 사용
4. value 값을 비교하여 left.val과 현재 val이 같으면 +1
5. 최대 값만 저장
"""


class Solution:
    # 클래스 변수 선언
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


root = [3, 5, 3, 5, 5, 3, None, 5, 1, 5, 2, 3]

node11 = TreeNode(root[11], None, None)
node10 = TreeNode(root[10], None, None)
node9 = TreeNode(root[9], None, None)
node8 = TreeNode(root[8], None, None)
node7 = TreeNode(root[7], None, None)
node5 = TreeNode(root[5], node11, None)
node4 = TreeNode(root[4], node9, node10)
node3 = TreeNode(root[3], node7, node8)
node2 = TreeNode(root[2], node5, None)
node1 = TreeNode(root[1], node3, node4)
node0 = TreeNode(root[0], node1, node2)


sol = Solution()

print("가장 긴 동일 값의 경로는", sol.longestUnivaluePath(node0), "입니다.")
