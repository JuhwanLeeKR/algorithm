# 혼자 작성할 수 있도록 연습하자
# 우리가 필요한 것 Node, Queue
class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next


class Queue:
    def __init__(self):
        # queue를 만들때는 앞에 있는 녀석을 지정해주는 것이 중요하다
        self.front = None

    def is_empty(self):
        return self.front is None

    def push(self, value):
        # 비어있는지 안 비어있는지 확인 먼저 해야한다
        if not self.front:
            self.front = Node(value, None)
            return

        # 안 비었다면 -> 끝까지 가야한다
        node = self.front
        # 다음이 존재하는 한 계속 간다
        while node.next:
            node = node.next

        # 끝에 도달한 상태이다
        node.next = Node(value, None)

    def pop(self):
        # 비어있는지 확인 먼저!
        if not self.front:
            return None
        # 제일 앞에 있는 녀석을 꺼내서
        node = self.front
        # front를 바꿔주기 위해 기존의 다음 node를 front로 지정한다
        self.front = self.next
        # node의 item을 꺼내준다
        return node.item
