# https://leetcode.com/problems/combinations/
# 1부터 n까지의 숫자가 주어질때, k개의 조합을 반환하라


"""
### wrong code
class Solution:
    def combine(self, n: int, k: int):  # -> list[list[int]]:
        numList = list(range(1, n + 1))
        stack = []
        result = []

        # stack에 numList의 요소를 전부 넣어 줍니다.
        for i in range(n):
            stack.append([numList[i]])
        #
        tmp = []
        for i in range(n):
            tmp.append(stack.pop())
            while stack:
                if i in tmp[i]:
                    break
                # stack에서 pop을 한게 tmp 입니다.

                if len(tmp) <= k:
                    tmp[i].append(numList[i])
                    break
                # tmp.append()

                print(tmp)

        print(stack)

        return numList
"""


class Solution:
    def combine(self, n: int, k: int):  # -> list[list[int]]:
        # stack을 사용할거라 스택을 선언해 줍니다.
        stack = []
        # 답변을 선언해 줍니다.
        answer = []
        # stack에 숫자를 숫자를 넣습니다.
        for num in range(n):
            stack.append([n - num])
        while stack:
            top = stack.pop()  # top: [1]
            # top의 길이가 k와 같아지면 answer에 추가해 줍니다.
            if len(top) == k:
                answer.append(top)
                # 아래 코드를 건너 띄어 줍니다.
                continue
            for i in range(n - top[-1]):
                stack.append(top + [n - i])
                print(n - top[-1], top + [n - i])
        return answer


n = 4
k = 3

sol = Solution()
sol.combine(n, k)
