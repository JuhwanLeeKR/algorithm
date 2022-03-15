# 206. Reverse Linked List
# Given the head of a singly linked list, reverse the list, and return the reversed list.
# https://leetcode.com/problems/reverse-linked-list/

# 타입힌트 Optional을 사용해주기 위해 import 해주어야한다.
import re
from typing import Optional

# Definition for singly-linked list.
# Tip: leet code를 긁어오면 주석 처리되어있다.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# leetcode input 값
head = [1, 2, 3, 4, 5]

# 1.역순의 연결리스트로 만들어주기 위해선 무엇을 해야할까?
# 2. sort 함수를 사용하여 역순으로 만들어주면 되지 않을까? Day.2 group-anagrams 참고 -> linked list이기 때문에 sort 함수가 먹히지 않는다.
# 3. 마지막 linked list 값을 가져와서 첫번째부터 새롭게 만들어준다.

# Tip) sorted함수는 새로운 정렬된 리스트를 반환하고, sort함수는 리스트 자체를 정렬 시켜버린다.


class Solution:
    def __init__(self):
        # 아무런 자료도 안들고 왔을때,
        self.head = None  # ListNode(None, None) 도 가능하다

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not self.head:
            # 다음 요소는 없고 입력받은 값이 head이다
            self.head = ListNode(head, None)

        # Tip) 확장 슬라이스 기능
        # https://docs.python.org/release/2.3.5/whatsnew/section-slices.html
        # head에 [::-1]을 해줘서 역순으로 배열을 반환한다
        head = head[::-1]  # [5,4,3,2,1]
        print(head)
        # 다시 linked list 값으로 반환해주어야합니다.
        node = self.head
        while node.next:
            node = node.next
        node.next = ListNode(head, None)

        # for e in reversHead:

        return head


solve = Solution()
print(solve.reverseList(head))
