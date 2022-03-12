class ListNode:
    # val: 내가 가진 값, next: 내가 가리키는 것
    def __init__(self, val, next):
        # 나의 value는 val이고,
        self.val = val
        # 나의 next는 next이다.
        self.next = next

# 연결 리스트 생성


class LinkedList:
    # 삽입(, 삭제도 있긴하지만 오늘은 삽입 기능만 한다)
    # init이 없어도 생성이 가능하고 pass를 이용할 수도 있다
    def __init__(self):
        # 아무런 자료도 안들고 왔을때,
        self.head = None  # ListNode(None, None) 도 가능하다

    def append(self, val):
        # 아직 입력받은 요소가 없을때
        if not self.head:
            # 다음 요소는 없고 입력받은 값이 head이다
            self.head = ListNode(val, None)
            return

        node = self.head
        while node.next:
            node = node.next
        node.next = ListNode(val, None)


# LinkedList화 시켜보기
lst = [1, 2, 3]
# l1이라는 linkedlist를 만들어준다.
l1 = LinkedList()
for e in lst:
    l1.append(e)
print(l1)


# 삭제는 직접 구현이나 구글링을 해본다.
